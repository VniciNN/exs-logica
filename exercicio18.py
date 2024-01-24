clientes = []

while True:
    cod = int(input("Digite o código do cliente: "))
    if cod == 0:
        break
    altura = float(input("Digite a Altura do cliente: "))
    peso = float(input("Digite o peso do cliente: "))
    cliente = {"código":cod, "altura":altura, "peso":peso}
    clientes.append(cliente)

print(clientes[0]['altura'])
