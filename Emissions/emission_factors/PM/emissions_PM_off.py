import pandas as pd
import re
import sys
import os

# Reconfigura a saída padrão para UTF-8 (opcional)
sys.stdout.reconfigure(encoding='utf-8')

# Define o diretório de trabalho como o diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Caminho para o arquivo, subindo três níveis
file_path = os.path.join("..", "..", "..", "TS_Project_SurveyUBike.xlsx")

# Carregar os dados
df = pd.read_excel(file_path, sheet_name='Raw data')


# Definir fatores de emissão (kg CO2 por km) para cada modo de transporte, incluindo combustíveis para carros
fatores_emissao = {
    'Car_Petrol': 0.011034502/1000/1.6,          # Real
    'Car_Diesel': 0.027780285/1000/1.6,          # Real
    'Car_LPG': 0.00248502/1000/1.6,             # Real
    'Bus': 0.190525295/1000/1.6,          # Real
    'Motorbike': 0.011034502/1000/1.6,           # Real
    'Walk': 0.0,
    'Bike': 0.0,
    'Rail': 0,                                   # Exemplo
    'Metro': 0,                                  # Exemplo
    'Ferry': 0,                                  # Exemplo
    'Taxi':  0.027780285/1000/1.6,               # Real
    'Carpool':  0.027780285/1000/2,              # Real
    'IST Shuttle':  0.027780285/1000/1.6         # Real
}


# 2. Verificar se a coluna 'Profile' existe
profile_column_name = 'Profile'  # Ajuste se necessário


# 3. Mapear Perfis para Probabilidades
perfil_prob = {
    1: 1.0,  # Willing - Muda totalmente para bicicleta
    2: 0.7,  # Willing se for elétrica (probabilidade de 30% de manter o transporte anterior)
    3: 0.4,  # Vai pensar (probabilidade de 60% de manter o transporte anterior)
    4: 0.0   # Não está willing (mantém totalmente o transporte anterior)
}

# 4. Definir Modos de Transporte e Mapeamento
# Mapeamento para a coluna 14:
# 1 - Walking; 2 - Car; 3 - Carpool; 4 - Bus; 5 - Ferry; 6 - Bike; 7 - Rail; 8 - Metro; 9 - Motorbike; 10 - IST Shuttle; 11 - Taxi; 12 - Other

modo_mapping = {
    '1': 'Walk',
    '2': 'Car',
    '3': 'Carpool',
    '4': 'Bus',
    '5': 'Ferry',
    '6': 'Bike',
    '7': 'Rail',
    '8': 'Metro',
    '9': 'Motorbike',
    '10': 'IST Shuttle',
    '11': 'Taxi',
    '12': 'Other'
}

# Lista de modos a considerar
modos = ['Car', 'Motorbike', 'Bus', 'Walk', 'Bike', 'Rail', 'Metro', 'Taxi', 'Other', 'Carpool', 'Ferry', 'IST Shuttle']

# Inicializar dicionário para contar shifters por modo
shift_dict = {modo: 0 for modo in modos}

# 5. Função para Identificar Modos de Transporte Atuais
def identificar_modos(row):
    modos_atuais = set()
    
    # Coluna 12: Uso de veículo privado
    uso_privado = row['Do you usually come to IST in your private vehicle? (no - 1; yes, with a car - 2; yes, with a motorbike - 3)']
    if uso_privado == 2:
        modos_atuais.add('Car')
    elif uso_privado == 3:
        modos_atuais.add('Motorbike')
    
    # Coluna 14: Modos combinados
    modos_combinados = row["In case you don't travel by car to IST, which modes are combined in your daily commuting? (1 - walking only; 2 - Private car; 3 - Carpool; 4 - Bus: 5 - Ferry; 6 - Bike; 7 - Rail; 8 - Metro; 9 - motorbike; 10 - IST Shutle; 11 - Taxi; 12 - Other)"]
    
    if pd.notnull(modos_combinados):
        modos_combinados_str = str(modos_combinados)
        # Extrair todos os números usando regex
        modos_combinados_lista = re.findall(r'\d+', modos_combinados_str)
        for modo_num in modos_combinados_lista:
            modo_name = modo_mapping.get(modo_num)
            if modo_name:
                modos_atuais.add(modo_name)
    
    return modos_atuais

# Função auxiliar para obter o modo de transporte com o pior fator de emissão
def obter_pior_modo(modos_atuais):
    
    # Excluir a bicicleta se estiver nos modos
    if 'Bike' in modos_atuais:
        modos_atuais.remove('Bike')
    
    # Se não sobrou nenhum outro modo além da bicicleta, retorna None
    if not modos_atuais:
        return None
    
    # Encontrar o modo com o pior fator de emissão (máximo)
    pior_modo = max(modos_atuais, key=lambda modo: fatores_emissao.get(modo, 0))
    return pior_modo

# Aplicar a função para criar a coluna 'Modos_Atuais'
df['Modos_Atuais'] = df.apply(identificar_modos, axis=1)

# 6. Calcular Shifters por Modo de Transporte, considerando apenas o pior modo
for index, row in df.iterrows():
    perfil = row[profile_column_name]
    prob = perfil_prob.get(perfil, 0)
    modos_atuais = row['Modos_Atuais']
    
    # Obter apenas o pior modo de transporte (em termos de emissões)
    pior_modo = obter_pior_modo(modos_atuais)
    
    # Continuar apenas se houver um modo válido (alguém que não usa bicicleta)
    if pior_modo and pior_modo in shift_dict:
        shift_dict[pior_modo] += prob

# Arredondar os contadores de shifters para números inteiros
shift_counts = {modo: round(count) for modo, count in shift_dict.items()}

# 7. Criar o Modal Shift Vector
modal_shift_vector = pd.DataFrame(list(shift_counts.items()), columns=['From Vehicle', 'To Cycling'])

print("Modal Shift Vector:")
print(modal_shift_vector)

# 8. Criar a Modal Shift Matrix
modal_shift_matrix = modal_shift_vector.set_index('From Vehicle').T
print("\nModal Shift Matrix:")
print(modal_shift_matrix)

# 9. Salvar os Resultados em Arquivos Excel
modal_shift_vector.to_excel("Modal_Shift_Vector.xlsx", index=False)
modal_shift_matrix.to_excel("Modal_Shift_Matrix.xlsx")

# 10. Calcular Emissões de CO₂ Antes e Depois da Mudança


# Renomear a coluna de distância para conveniência
distance_column_original = 'What is the travel distance of your commuting trip? (km)'
distance_column_new = 'Travel_Distance_km'

df = df.rename(columns={distance_column_original: distance_column_new})

# Função para identificar o combustível do carro
def identificar_combustivel(row):
    tipo_combustivel = row["What is the fuel type of your car (if you use car to come to IST)? (Diesel or Diesel Hybrid - 1; Petrol or Hybrid petrol - 2; LPG - 3; Electric - 4)"]
    
    if tipo_combustivel == 1:
        return 'Car_Diesel'
    elif tipo_combustivel == 2:
        return 'Car_Petrol'
    elif tipo_combustivel == 3 or tipo_combustivel == 4:  # Tratando "Electric" como "LPG" por falta de dados
        return 'Car_LPG'
    else:
        return None
    
    # Função para obter a velocidade média com base no pior modo de transporte
def obter_velocidade_pior_modo(pior_modo):
    if pior_modo == 'Car':
        return 25  # km/h para carro
    elif pior_modo == 'Bus':
        return 15  # km/h para autocarro
    else:
        return 10  # km/h para outros modos, se necessário

# Função para calcular a distância usando o tempo e a velocidade do pior modo
def calcular_distancia_se_nao_informado(row):
    if pd.isna(row[distance_column_new]):  # Verificar se a distância está em branco
        pior_modo = obter_pior_modo(row['Modos_Atuais'])
        velocidade = obter_velocidade_pior_modo(pior_modo)
        tempo_viagem_horas = row['What is your usual travel time to IST, from home? (minutes)'] / 60  # Converter minutos para horas
        return velocidade * tempo_viagem_horas  # Distância estimada
    return row[distance_column_new]

# Aplicar a função para preencher as distâncias ausentes
df[distance_column_new] = df.apply(calcular_distancia_se_nao_informado, axis=1)

# Atualizar a função de calcular emissões antes da mudança
def calcular_emissao_antes(row):
    emissao = 0.0
    modos_atuais = row['Modos_Atuais']
    distancia_total = row[distance_column_new]
    
    # Obter o pior modo de transporte, ou seja, aquele com maior emissão de CO2
    pior_modo = obter_pior_modo(modos_atuais)
    
    if pior_modo:
        if pior_modo == 'Car':
            combustivel = identificar_combustivel(row)
            if combustivel:
                emissao += fatores_emissao[combustivel] * distancia_total
        else:
            emissao += fatores_emissao[pior_modo] * distancia_total
    
    return emissao

# Atualizar a função de calcular emissões após a mudança
def calcular_emissao_depois(row):
    emissao = 0.0
    perfil = row[profile_column_name]
    prob = perfil_prob.get(perfil, 0)
    modos_atuais = row['Modos_Atuais']
    distancia_total = row[distance_column_new]
    
    # Obter o pior modo de transporte
    pior_modo = obter_pior_modo(modos_atuais)
    
    if pior_modo:
        if pior_modo == 'Car':
            combustivel = identificar_combustivel(row)
            if combustivel:
                emissao += distancia_total * fatores_emissao[combustivel] * (1 - prob)
        else:
            emissao += distancia_total * fatores_emissao[pior_modo] * (1 - prob)
    
    return emissao

# Calcular emissões antes e depois
df['Emissao_Antes'] = df.apply(calcular_emissao_antes, axis=1)
df['Emissao_Depois'] = df.apply(calcular_emissao_depois, axis=1)

# Somar as emissões totais antes e depois
emissoes_totais_antes = df['Emissao_Antes'].sum()
emissoes_totais_depois = df['Emissao_Depois'].sum()

# Calcular a redução total de emissões
reducao_emissoes = emissoes_totais_antes - emissoes_totais_depois

print(f"\nEmissões Totais Antes: {round(emissoes_totais_antes, 2)} kg PM (off)")
print(f"Emissões Totais Depois: {round(emissoes_totais_depois, 2)} kg PM (off)")
print(f"Redução de Emissões: {round(reducao_emissoes, 2)} kg PM (off)")
print(f"Redução em percentagem: {round(reducao_emissoes/emissoes_totais_antes*100)} %")

