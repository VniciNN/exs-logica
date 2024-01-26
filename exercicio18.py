clientes = []
alturas = []
pesos = []
maior_altura = []
menor_altura = []
menor_peso = []
maior_peso = []


while True:
    cod = int(input("Digite o código do cliente: "))
    if cod == 0:
        break
    altura = float(input("Digite a Altura do cliente: "))
    peso = float(input("Digite o peso do cliente: "))
    cliente = {"código":cod, "altura":altura, "peso":peso}
    clientes.append(cliente)

for i in range(len(clientes)):
    alturas.append(clientes[i].get('altura'))
    pesos.append(clientes[i].get('peso'))

maior_altura.append(max(alturas))
menor_altura.append(min(alturas))
maior_peso.append(max(pesos))
menor_peso.append(min(pesos))

for i in range(len(clientes)):
    if maior_altura[0] == clientes[i].get('altura'):
        maior_altura.clear()
        maior_altura = clientes[i]
        break

for i in range(len(clientes)):
    if menor_altura[0] == clientes[i].get('altura'):
        menor_altura.clear()
        menor_altura = clientes[i]
        break

for i in range(len(clientes)):
    if maior_peso[0] == clientes[i].get('peso'):
        maior_peso.clear()
        maior_peso = clientes[i]
        break

for i in range(len(clientes)):
    if menor_peso[0] == clientes[i].get('peso'):
        menor_peso.clear()
        menor_peso = clientes[i]
        break

media_peso = sum(pesos) / len(pesos)
media_altura = sum(alturas) / len(alturas)

print(f'Cliente de maior altura: {maior_altura}')
print(f'Cliente de menor altura: {menor_altura}')
print(f'Cliente de maior peso: {maior_peso}')
print(f'Cliente de menor peso: {menor_peso}')
print(f'Média altura: {media_altura}')
print(f'Média peso: {media_peso}')