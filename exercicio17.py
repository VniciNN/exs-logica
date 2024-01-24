while True: 
    valores = []
    produto = 1
    while True:
        valor = float(input(f'Digite o valor do produto {produto}: '))
        if valor == 0:
            break
        valores.append(valor)
        produto += 1
    total