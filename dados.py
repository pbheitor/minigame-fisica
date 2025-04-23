import json
import os

progresso_arquivo = "progresso.json"
ranking_arquivo = "ranking.json"

def criar_novo_jogo(nome_arquivo="progresso.json"):
    progresso = {
        "vidas": 3,
        "pontos": 0,
        "nivel": "Novato",
        "pulos": 1,
        "dicas": 0
    }

    salvar_progresso(progresso, nome_arquivo, mostrar_mensagem=False)
    return progresso


def carregar_progresso(nome_arquivo="progresso.json"):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            progresso = json.load(arquivo)

            if "dicas" not in progresso:
                progresso["dicas"] = 0
            if "pulos" not in progresso:
                progresso["pulos"] = 1
            if "vidas" not in progresso:
                progresso["vidas"] = 3
            if "pontos" not in progresso:
                progresso["pontos"] = 0
            if "nivel" not in progresso:
                progresso["nivel"] = "Novato"

            return progresso
    return {
    "vidas": 3,
    "pontos": 0,
    "nivel": "Novato",
    "pulos": 1,
    "dicas": 0
    }

def salvar_progresso(progresso, nome_arquivo="progresso.json", mostrar_mensagem=True):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(progresso, arquivo)
    if mostrar_mensagem:
        print("Progresso salvo!")

def atualizar_nivel(progresso):
    if progresso["pontos"] >= 350:
        progresso["nivel"] = "Mestre de Física"
    elif progresso["pontos"] >= 150:
        progresso["nivel"] = "Intermediário"
    elif progresso["pontos"] >= 50:
        progresso["nivel"] = "Iniciante"
    else:
        progresso["nivel"] = "Novato"
    return progresso

