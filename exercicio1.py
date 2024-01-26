def preencher_lista(lista):
    for i in range(10):
        number = int(input("Digite um número: "))
        lista.append(number)
        return lista

def exibir_lista(lista):
    for i in range(len(lista)):
        print(lista[i])

lista = []

exibir_lista(preencher_lista(lista))
