def validacao(dono, morador, carteira_ind, autorizacao_morador):
    if morador == True and carteira_ind == True:
        return True
    elif dono == True: 
        return True
    elif morador == False and autorizacao_morador == True:
        return True
    else:
        return False