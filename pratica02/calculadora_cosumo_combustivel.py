# Calculadora de Consumo de Combustível
distancia = 500
combustivel_gasto = 35

consumo_medio = round(distancia / combustivel_gasto, 2)

print("Dados da viagem:")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio} km/l")