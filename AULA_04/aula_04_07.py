# Construa um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.

# Entrada de Dados
n = int(input("Digite um número inteiro: "))

# Processamento dos Dados
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i

# Saída de Dados
print(f"O fatorial de {n} é: {fatorial}")