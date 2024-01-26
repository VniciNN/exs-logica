clientes = []
alturas = []
pesos = []
maior_altura = []
menor_altura = []
menor_peso = []
maior_peso = []

def cadastro():
    while True:
        cod = int(input("Digite o código do cliente: "))
        if cod == 0:
            break
        altura = float(input("Digite a Altura do cliente: "))
        peso = float(input("Digite o peso do cliente: "))
        cliente = {"código":cod, "altura":altura, "peso":peso}
        clientes.append(cliente)

def add_pesos_alturas(alturas, pesos):
    for i in range(len(clientes)):
        alturas.append(clientes[i].get('altura'))
        pesos.append(clientes[i].get('peso'))
    maior_altura.append(max(alturas))
    menor_altura.append(min(alturas))
    maior_peso.append(max(pesos))
    menor_peso.append(min(pesos))

def obtendo_info(info, caract_fis):
    for i in range(len(clientes)):
        if info[0] == clientes[i].get(caract_fis):
            info.clear()
            info = clientes[i]
            return info

def calcula_media():
    media_peso = sum(pesos) / len(pesos)
    media_altura = sum(alturas) / len(alturas)
    return media_altura, media_peso

def exibicao(media_altura, media_peso, codigo, altura, peso):
    print(f'Cliente de maior altura: Código: {maior_altura.get(codigo)}, Altura: {maior_altura.get(altura)}, Peso: {maior_altura.get(peso)}')
    print(f'Cliente de menor altura: Código: {menor_altura.get(codigo)}, Altura: {menor_altura.get(altura)}, Peso: {menor_altura.get(peso)}')
    print(f'Cliente de maior peso:  Código: {maior_peso.get(codigo)}, Altura: {maior_peso.get(altura)}, Peso: {maior_peso.get(peso)}')
    print(f'Cliente de menor peso:  Código: {menor_peso.get(codigo)}, Altura: {menor_peso.get(altura)}, Peso: {menor_peso.get(peso)}')
    print(f'Média altura: {media_altura}')
    print(f'Média peso: {media_peso}')

cadastro()
add_pesos_alturas(alturas, pesos)
maior_altura = obtendo_info(maior_altura, 'altura')
menor_altura = obtendo_info(menor_altura, 'altura')
maior_peso = obtendo_info(maior_peso, 'peso')
menor_peso = obtendo_info(menor_peso, 'peso')
media = calcula_media()
exibicao(media[0], media[1], 'código', 'altura', 'peso')