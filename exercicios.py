import json
import random

exercicios_arquivo = "exercicios.json"

def carregar_exercicios():
    try:
        with open(exercicios_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except Exception as e:
        print(f"Erro ao carregar exercícios: {e}")
        return []

exercicios = carregar_exercicios()

def escolher_exercicio():
    if not exercicios:
        return None
    return random.choice(exercicios)

def obter_resposta_correta(exercicio_id):
    for exercicio in exercicios:
        if exercicio["id"] == exercicio_id:
            return exercicio["resposta_final"]
    return None




