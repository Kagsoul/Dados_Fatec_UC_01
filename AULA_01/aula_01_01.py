# Faça um programa que obtenha o valor para a variável HT (horas trabalhadas no mês), obtenha o valor para a variável VH (valor hora trabalhada), obtenha o valor para a variável PD (percentual de desconto) e calcule o salário bruto => SB = HT * VH, mais o total de desconto => TD = (PD/100)*SB e o salário líquido => SL = SB – TD. Apresentando ao final o Salário Liquido.

# Entrada de Dados
ht = int(input("Digite a quantidade de horas trabalhadas: "))
vh = float(input("Digite o valor da hora trabalhada: "))
pd = float(input("Digite o percentual de desconto: "))

# Processamento dos Dados
sb = ht * vh
td = (pd / 100) * sb
sl = sb - td

# Saída de Dados
print(f"O Salário Bruto é R$ {sb:.2f}")

print(f"O Total de Desconto é: {td:.2f}")

print(f"O Salário Líquido é R$ {sl:.2f}")  

#este e dificil, mas aprendi bem a funcionalidade do .2f dentro da chave, e muito importante para o script com matematica efetue R$\dinheiro