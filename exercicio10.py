def demissao(exp_meses, vendas):
    if exp_meses < 6:
        return True
    elif exp_meses < 24 and vendas < 5000:
        return True
    elif exp_meses < 60 and vendas < 250000:
        return True
    else:
        return False

