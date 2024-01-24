lista = []

for _ in range(10):
    number = int(input("Digite um número: "))
    lista.append(number)

for i in range(len(lista)):
    if lista[i] >= 10:
        print(lista[i])

