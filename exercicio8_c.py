def validacao(qtd_portas, preco, ano):
    if qtd_portas == 4 and preco > 20000 and preco < 50000 and ano == 2024:
        return True
    else: 
        return False
    