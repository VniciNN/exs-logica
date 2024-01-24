def validacao(origem, preco, tipo):
    if origem == "F" or origem == "I" and preco > 500:
        return True
    elif origem == "P" and preco > 800 and tipo != "V":
        return False
    else:
        return False