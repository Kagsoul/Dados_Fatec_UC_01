# Faça um programa que pergunte a uma pessoa, a sua idade, o seu peso e quanto dormiu nas últimas 24 h e diga se ela pode doar ou não sangue de acordo com as seguintes condições: 
# • Ter entre 16 e 69 anos. 
# • Pesar mais de 50 kg.
# • Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).

# Entrada dos dados
idade = int(input('Informe a sua idade: '))
peso = float(input('Informe o seu peso: '))
sono = int(input('Informe a quantidade de horas de sono: '))

# Processamento dos dados
if (idade >= 16 and idade <= 69) and peso >= 50 and sono >= 6:
    print('Você está APTO a doar')
elif idade < 16 or idade > 69:
    print('Você não está APTO a doar, pois sua idade não é compatível')
elif peso < 50:
    print('Você não está APTO a doar, pois seu peso não é compatível')
else:
    print('Você não está APTO a doar, pois sua quantidade de sono não é compatível')