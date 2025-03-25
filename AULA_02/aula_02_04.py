# Crie um programa que calcule a idade de uma pessoa a partir do ano de nascimento dela.

# Importando a biblioteca de data e hora
import datetime

# Entrada dos Dados
data_atual = datetime.date.today()
ano_nasc = int(input('Informe o ano de nascimento: '))
ano_atual = data_atual.year

# Processamento dos Dados
idade = ano_atual - ano_nasc

# Saída dos Dados
print(f'A sua idade é {idade} anos.')