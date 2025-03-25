# Escreva um programa que calcule a velocidade média de um veículo com base na distância percorrida e no tempo em que uma viagem foi realizada. Assim como a quantidade de combustível gasto nessa viagem, sabendo que o veículo usado consome 12 Km/l.

# Entrada dos Dados
cm = 12
d = int(input("Informe a distância percorrida (Km) :"))
t = float(input("Informe o tempo de viagem (Horas) :"))

# Processamento dos Dados
vm = d / t
l = d / cm

# Saída dos Dados
print(f"A velocidade média do veículo foi {vm} Km/h.")
print(f"A quantidade gasta de combustível foi {l:.1f} litros.")