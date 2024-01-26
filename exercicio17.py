while True: 
    valores = []
    produto = 1
    while True:
        valor = float(input(f'Digite o valor do produto {produto}: '))
        if valor == 0:
            break
        valores.append(valor)
        produto += 1
    total = sum(valores)
    dinheiro = float(input("Digite a quatidade de dinheiro entregue pelo cliente: "))
    troco = dinheiro - total
    for i in range(len(valores)):
        print(f'Produto {i + 1}: {valores[i]}')
    print(f'Total: {total}')
    print(f'Dinheiro: {dinheiro}')
    print(f'Troco: {troco}')