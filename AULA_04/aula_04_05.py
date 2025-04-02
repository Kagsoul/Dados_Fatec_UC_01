# Utilizando apenas o conceito de repetição, faça um programa para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, pois o segundo valor não pode ser igual a zero. Ao final imprimir o resultado da divisão do primeiro valor pelo segundo valor.

# Entrada de Dados
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))

# Processamento dos Dados
while n2 == 0:
    n2 = int(input("Digite o segundo valor: "))

# Saída de Dados
print(f"O resultado da divisão de {n1} por {n2} é: {(n1 / n2):.2f}")