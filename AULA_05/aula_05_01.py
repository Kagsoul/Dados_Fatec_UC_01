nomes = "Alessandro, Maria, Eduarda"
nomes_lista = ["Alessandro","Maria","Eduarda"]
num = []

for i in range(5):
    num.append(int(input("Informe um Valor Inteiro: ")))

for i in range(len(num)):
    print(f"O número {num[i]} está na posição {i} da lista")

print(num)
print("------------------")
print(nomes)
print(nomes_lista)
print(nomes_lista[2])