import sys

# Reconfigura a saída padrão para UTF-8 (opcional)
sys.stdout.reconfigure(encoding='utf-8')

## CAR
# Gasolina (kms and stock)
kms_gasolina = [
    7619, 3298, 2663, 1332, 0, 909, 1053, 1465, 2914, 4750, 0, 0,
    6548, 7486, 8263, 8261, 4832, 5135, 2567, 0, 1010, 1074, 2129,
    3508, 5931, 0, 0, 7209, 8641, 8963, 8436, 5184, 3158, 1579, 0,
    1013, 1338, 2554, 3426, 5532, 6929, 8138, 8563, 8123, 7096, 9727,
    4863, 0, 0, 0, 0, 0, 0, 0, 705, 1067, 16334, 16334, 0, 4997,
    2688, 16334, 16334, 0, 416, 4786, 16334, 16334, 0
]
stock_gasolina = [
    7619, 3298, 2663, 1332, 0, 909, 1053, 1465, 2914, 4750, 0, 0, 6548, 7486, 8263, 
    8261, 4832, 5135, 2567, 0, 1010, 1074, 2129, 3508, 5931, 0, 0, 7209, 8641, 8963, 
    8436, 5184, 3158, 1579, 0, 1013, 1338, 2554, 3426, 5532, 6929, 8138, 8563, 8123, 
    7096, 9727, 4863, 0, 0, 0, 0, 0, 0, 0, 705, 1067, 16334, 16334, 0, 4997, 2688, 
    16334, 16334, 0, 416, 4786, 16334, 16334, 0
]


# Gasoleo (kms and stock)
kms_gasoleo = [
    8993, 8174, 10253, 5127, 0, 6402, 9078, 10323, 10431, 11214, 13513, 29505, 14752, 0, 
    7669, 9090, 10969, 11687, 12273, 13856, 25463, 12731, 0, 8649, 10052, 10472, 12324, 
    14033, 14563, 17473, 8736, 0
]
stock_gasoleo = [
    6983, 5459, 2559, 1637, 0, 16156, 25096, 32352, 71984, 52404, 75010, 31759, 31671, 0, 
    10895, 53159, 132045, 276386, 391897, 278761, 58318, 61106, 0, 40900, 53827, 187247, 
    232779, 248548, 149505, 41069, 40850, 0
]


# LPG (kms and stock)
kms_lpg = [
    13230, 13551, 11801, 4925, 11819, 11668, 13247, 13101,
    13326, 11801, 5175, 11666, 11749, 13248, 13123, 13326,
    11801, 4526, 11783, 11797, 13229, 12807, 13268, 11801
]
stock_lpg = [
    45, 64, 45, 5314, 5966, 5161, 2084, 422, 966, 686, 1021, 4050, 7100, 4829, 856,
    1665, 1252, 1493, 2112, 3700, 1397, 272, 1029, 786
]

# Buses (kms and stock)
kms_buses = [
    8305, 12692, 15509, 22414, 23668, 22670, 15029, 12563, 17534, 20109, 29590, 
    48929, 47574, 16952, 12045, 15016, 22559, 34421, 50364, 56144, 50309, 12563, 
    17534, 20109, 29590, 48929, 47574, 16952, 12045, 15016, 22559, 34421, 50364, 
    56114, 50309, 56070, 0, 220987, 215977, 0, 0, 0, 0, 0, 0, 0
]
stock_buses = [
    283, 132, 899, 1554, 1147, 566, 481, 382, 128, 292, 205, 49, 51, 17, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 34, 89, 0, 0, 0, 0, 0, 0, 0
]

############################################################ peak


emissions_cars_gasolina_peak = 31.964649636664401209 + 0.122447190274785828
print(f"Fator de emissão PM (g/km*V) para carros a gasolina em peak hours = {round(1e6 * emissions_cars_gasolina_peak/sum(k * s for k, s in zip(kms_gasolina, stock_gasolina)), 9)}")


emissions_cars_gasoleo_peak = 990.02414114682088698
print(f"Fator de emissão PM (g/km*V) para carros a gasoleo em peak hours = {round(1e6 * emissions_cars_gasoleo_peak/sum(k * s for k, s in zip(kms_gasoleo, stock_gasoleo)), 9)}")


emissions_cars_lpg_peak = 1.4445516958948271630
print(f"Fator de emissão PM (g/km*V) para carros a lpg em peak hours = {round(1e6 * emissions_cars_lpg_peak/sum(k * s for k, s in zip(kms_lpg, stock_lpg)), 9)}")


############################################################ off

emissions_cars_gasolina_off = 31.964641427114141758 + 0.122447178612446797
print(f"Fator de emissão PM (g/km*V) para carros a gasolina em off hours = {round(1e6 * emissions_cars_gasolina_off/sum(k * s for k, s in zip(kms_gasolina, stock_gasolina)), 9)}")


emissions_cars_gasoleo_off = 922.53125339604375390
print(f"Fator de emissão PM (g/km*V) para carros a gasolina em off hours = {round(1e6 * emissions_cars_gasoleo_off/sum(k * s for k, s in zip(kms_gasoleo, stock_gasoleo)), 9)}")


emissions_cars_lpg_off = 1.4445514788518652012
print(f"Fator de emissão PM (g/km*V) para carros a lpg em off hours = {round(1e6 * emissions_cars_lpg_off/sum(k * s for k, s in zip(kms_lpg, stock_lpg)), 9)}")

## BUSES
emissions_buses = 27.4010236707565724
print(f"Fator de emissão PM (g/km*V) para autocarros = {round(1e6 * emissions_buses/sum(k * s for k, s in zip(kms_buses, stock_buses)), 9)}")