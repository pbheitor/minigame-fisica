from exercicios import obter_resposta_correta

def normalizar_texto(texto):
    return texto.replace(" ", "").lower()

def verificar_resposta(exercicio_id, resposta_usuario):
    resposta_correta = obter_resposta_correta(exercicio_id)

    if resposta_correta is None:
        return False
    
    resposta_normalizada = normalizar_texto(resposta_usuario)
    correta_normalizada = normalizar_texto(resposta_correta)


    return resposta_normalizada == correta_normalizada