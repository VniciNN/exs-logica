while True: 
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    if nome == senha:
        print("Digite uma senha diferente do nome de usuário")
    else: 
        print("Tudo ok")
        break