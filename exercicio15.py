cont = "sim"

while cont == "sim":
    valor = int(input("Deseja a tabuada de qual valor?: "))
    
    for i in range(11):
        print(f'{valor} x {i} = {valor * i}')
    
    cont = input("Deseja continuar? (caso queira, digite sim): ").lower()

print("Programa encerrado!!")