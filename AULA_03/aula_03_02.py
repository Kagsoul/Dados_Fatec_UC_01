# Tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas: 
#* Para homens: (72.7*h) - 58
#* Para mulheres: (62.1*h) - 44.7

# Entrada dos Dados
nome = input('Informe o seu nome: ')
altura = float(input('Informe a sua altura em metros: '))
sexo = input('Informe M para Masculino ou F para Feminino :')

# Processamento dos Dados
if sexo == 'M' or sexo == 'm':
    h = (72.7*altura) - 58
    print(f'Sr(a) {nome}, seu peso ideal é {h:.0f} Kg.')
elif sexo == 'F' or sexo == 'f':
    m = (62.1*altura) - 44.7
    print(f'Sr(a) {nome}, seu peso ideal é {m:.0f} Kg.')
else:
    print('Verifique o sexo informado')


