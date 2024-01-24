lista = []

for _ in range(20):
    number = float(input("Digite um número: "))
    lista.append(number)

soma = 0

for i in range(10):
    soma += lista[i]

print(soma)