def coletar_nome():
    while True:
        nome = input("Digite seu nome: ")
        if len(nome) > 3:
            return nome
        else:
            print("O nome precisa ter mais de 3 caracteres")

def coletar_idade():
    while True:
        idade = int(input("Digite sua idade: "))
        if idade >= 0 and idade <= 150:
            return idade
        else: 
            print("Digite uma idade válida")

def coletar_salario():
    while True:
        salario = float(input("Digite seu salario: "))
        if salario > 0:
            return salario
        else:
            print("Digite um salário maior que zero")

def coletar_sexo(): 
    while True:
        sexo = input("Digite o seu sexo(f ou m): ")
        if sexo == "f" or sexo == "m":
            return sexo
        else:
            print("Digite um sexo válido")
    
def coletar_estado_civil():
    while True:
        estado_civil = input("Digite seu estado civil(s, c, v, d): ")
        if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
            return estado_civil
        else:
            print("Difite um estado de civil válido")

nome = coletar_nome()
idade = coletar_idade()
salario = coletar_salario()
sexo = coletar_sexo()
estado_civil = coletar_estado_civil()

print(nome, idade, salario, sexo, estado_civil)