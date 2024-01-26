def media(n1, n2, n3, n4, n5): 
    media = (n1 + n2 + n3 + n4 + n5) / 5
    return media

def aprovacao_aluno(media):
    if media >= 7:
        resultado = "Aprovado"
    elif media < 7 and media >= 4:
        resultado = "Avaliação Final"
        return resultado
    else: 
        resultado = "Reprovado"
        return resultado
    
media = media()
print(aprovacao_aluno(media))