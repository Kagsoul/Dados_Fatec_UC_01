idade = int(input("Informe a sua Idade: "))
if idade < 18:
    print("Você é Menor de Idade")
elif idade == 18:
    print("Você tem exatos 18 anos - Acesso Liberado")
elif idade > 18 and idade < 65:
    print("Acesso Liberado")
else:
    print("Você tem mais de 65 anos - Acesso Liberado com Cautela")