# Construa um programa que calcule e mostre a tabuada de um número inteiro fornecido pelo usuário.

# Entrada de Dados
n = int(input("Digite um número inteiro: "))

# Processamento dos Dados
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")  