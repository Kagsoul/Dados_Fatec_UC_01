# Faça um programa que leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em Celsius

# Entrada dos Dados 
c = float(input("Informe uma temperatura em graus o.C: "))

# Processamento dos Dados
f = (9 * c + 160) / 5

# Saída dos Dados
print(f"A temperatura em graus o.F é {f:.1f}")