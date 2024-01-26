lista = []
lista_b = []

for i in range(8):
    number = int(input("Digite um número: "))
    lista.append(number)
    lista_b.append(number * 3)

for i in range(len(lista_b)):
    print(lista_b[i])