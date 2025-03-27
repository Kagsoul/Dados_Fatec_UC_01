# Escreva um programa que, dados 3 números inteiros (n1, n2 e n3), diga qual deles é maior.

# Entrada de dados
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))

# Processamento e saída de dados
if n1 > n2 and n1 > n3:
    print(f'O maior valor é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior valor é {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior valor é {n3}')
else:
    print('Existem pelo menos dois valores iguais')
