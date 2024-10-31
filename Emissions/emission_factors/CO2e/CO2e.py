import sys

# Reconfigura a saída padrão para UTF-8 (opcional)
sys.stdout.reconfigure(encoding='utf-8')


#GASOLINA
#################### peak
fator_emissao_gasolina_CO2 = 1069.395676151
fator_emissao_gasolina_CH4 = 0.064978002
fator_emissao_gasolina_N2O = 0.030774959
fator_emissao_gasolina_peak_CO2e = fator_emissao_gasolina_CO2 + 28 * fator_emissao_gasolina_CH4 + 265 * fator_emissao_gasolina_N2O
#################### off
fator_emissao_gasolina_CO2 = 973.854574269
fator_emissao_gasolina_CH4 = 0.064978002
fator_emissao_gasolina_N2O = 0.030774959
fator_emissao_gasolina_off_CO2e = fator_emissao_gasolina_CO2 + 28 * fator_emissao_gasolina_CH4 + 265 * fator_emissao_gasolina_N2O



#GASOLEO
#################### peak
fator_emissao_gasoleo_CO2 = 210.390793209
fator_emissao_gasoleo_CH4 = 0.001812252
fator_emissao_gasoleo_N2O = 0.005790856
fator_emissao_gasoleo_peak_CO2e = fator_emissao_gasoleo_CO2 + 28 * fator_emissao_gasoleo_CH4 + 265 * fator_emissao_gasoleo_N2O
#################### off
fator_emissao_gasoleo_CO2 = 194.832863417
fator_emissao_gasoleo_CH4 = 0.001813149
fator_emissao_gasoleo_N2O = 0.005790856
fator_emissao_gasoleo_off_CO2e = fator_emissao_gasoleo_CO2 + 28 * fator_emissao_gasoleo_CH4 + 265 * fator_emissao_gasoleo_N2O



#LPG
#################### peak
fator_emissao_lpg_CO2 = 183.009715291
fator_emissao_lpg_CH4 = 0.020784902
fator_emissao_lpg_N2O = 0.007631377
fator_emissao_lpg_peak_CO2e = fator_emissao_lpg_CO2 + 28 * fator_emissao_lpg_CH4 + 265 * fator_emissao_lpg_N2O
#################### off
fator_emissao_lpg_CO2 = 172.318794669
fator_emissao_lpg_CH4 = 0.020784902
fator_emissao_lpg_N2O = 0.007631377
fator_emissao_lpg_off_CO2e = fator_emissao_lpg_CO2 + 28 * fator_emissao_lpg_CH4 + 265 * fator_emissao_lpg_N2O



#BUSES
#################### peak
fator_emissao_buses_CO2 = 1126.367295562
fator_emissao_buses_CH4 = 0.260915661
fator_emissao_buses_N2O = 0.0308455
fator_emissao_buses_CO2e = fator_emissao_buses_CO2 + 28 * fator_emissao_buses_CH4 + 265 * fator_emissao_buses_N2O

#CH4 -> 21
#N2O -> 310


print(f"Fator de emissão para CO2e (g/km*V) para carros a gasolina em peak hours = {fator_emissao_gasolina_peak_CO2e/1.6}")
print(f"Fator de emissão para CO2e (g/km*V) para carros a gasoleo em peak hours = {fator_emissao_gasoleo_peak_CO2e/1.6}")
print(f"Fator de emissão para CO2e (g/km*V) para carros a lpg em peak hours = {fator_emissao_lpg_peak_CO2e/1.6}")
print(f"Fator de emissão para CO2e (g/km*V) para carros a gasolina em off hours = {fator_emissao_gasolina_off_CO2e/1.6}")
print(f"Fator de emissão para CO2e (g/km*V) para carros a gasoleo em off hours = {fator_emissao_gasoleo_off_CO2e/1.6}")
print(f"Fator de emissão para CO2e (g/km*V) para carros a lpg em off hours = {fator_emissao_lpg_off_CO2e/1.6}")
print(f"Fator de emissão para CO2e (g/km*V) para autocarros = {fator_emissao_buses_CO2e/20.3}")