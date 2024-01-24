lista = []

for _ in range(10):
    number = int(input("Digite um número inteiro: "))
    lista.append(number)

print("-"*10)

a = int(input("Digite um número inteiro: "))
b = int(input("Digite um número inteiro: "))
c = int(input("Digite um número inteiro: "))

count = 0

for i in range(len(lista)):
    if lista[i] == a or lista[i] == b or lista[i] == c:
        count += 1

print(count)