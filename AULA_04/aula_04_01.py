n = 0
while n <= 5:
    print(n)
    n += 1 # n = n + 1

for i in range(5):
    print(i)

n = 0
resp = "S"
while resp == "S" or resp == "s":
    print(n)
    n = n + 1
    resp = input('Deseja Continuar(S/N)? ')