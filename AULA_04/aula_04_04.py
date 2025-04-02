# Construa um programa onde serão fornecidas as duas notas de dez alunos. Calcule a média de cada aluno e mostre a situação de cada aluno de acordo com as seguintes condições:
# - Se a média for maior igual a 70 -> ATENDIDO
# - Se a média for maior igual a 30 e menor que 70 -> PARCIALMENTE ATENDIDO
# - Se a média for menor que 30 -> NÃO ATENDIDO

# Entrada dos dados

# Processamento dos dados - Estrutura de Repetição
for i in range(3):
    nome = input('Informe o Nome do Estudante: ')
    nota_01 = float(input(f'Informe a Primeira Nota do estudante {nome} :'))
    nota_02 = float(input(f'Informe a Segunda Nota do estudante {nome} :'))

    media = (nota_01 + nota_02) / 2

    if media >= 70:
        situacao = "ATENDIDO"
    elif media >= 30 and media < 70:
        situacao = "PARCIALMENTE ATENDIDO"
    else:
        situacao = "NÃO ATENDIDO"
    
    print(f'Sr(a) {nome} a sua média foi {media:.2f}, portanto você está {situacao}')

