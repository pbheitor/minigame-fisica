import time
import os
from exercicios import escolher_exercicio
from verificador import verificar_resposta
from dados import salvar_progresso, carregar_progresso, atualizar_nivel, criar_novo_jogo

def menu():
    pass

progresso_existe = False
escolha = int(input("1 - Novo jogo\n2 - Carregar jogo\nEscolha: ").strip())
if escolha == 1:
    nome_save = input("Nome do save: ").strip()
    progresso = criar_novo_jogo("progresso_"+nome_save+".json")
else:
    while progresso_existe is False:
        nome_save = input("Nome do save: ").strip()
        caminho = "progresso_"+nome_save+".json"

        if os.path.exists(caminho):
            progresso_existe = True
            progresso = carregar_progresso("progresso_"+nome_save+".json")
        else:
            print("O progresso não existe.")
menu()


tempo_limite = 600  # 10 minutos

def iniciar_jogo():
    global progresso

    primeira_vez = True
    continuar = True

    while continuar:
        if not primeira_vez:
            continuar_input = input("\nDeseja responder outra questão? (s/n): ").strip().lower()
            if continuar_input != "s":
                print("Voltando ao menu principal...")
                break
        else:
            primeira_vez = False

        exercicio = escolher_exercicio()

        if not exercicio:
            print("Nenhum exercício disponível!")
            break

        print(f"\n{exercicio['pergunta']}")
        print("Você tem até 10 minutos para resolver essa questão fora do programa.")
        print("Durante a questão, você pode digitar:")
        print("  /pular → para pular (se tiver pulos)")
        print("  /dica → para ver uma dica (se tiver dicas)\n")

        inicio = time.time()
        
        while True:
            resposta_usuario = input("Digite a resposta final: ").strip().lower()

            if resposta_usuario == "/pular":
                if progresso["pulos"] > 0:
                    progresso["pulos"] -= 1
                    print("Questão pulada! Nenhuma penalidade aplicada.")
                    salvar_progresso(progresso, mostrar_mensagem=False)
                    break
                else:
                    print("Você não tem pulos disponíveis.")
            elif resposta_usuario == "/dica":
                if progresso['dicas'] > 0:
                    print(f"Dica: {exercicio['dica']}")
                    progresso['dicas'] -= 1
                    salvar_progresso(progresso, mostrar_mensagem=False)
                else:
                    print("Você não tem dicas disponíveis.")
            else:
                fim = time.time()
                break
        
        if resposta_usuario not in ["/pular", "/dica"]:
            tempo_gasto = fim - inicio

            if tempo_gasto > tempo_limite:
                print(f"\nTempo esgotado! Você levou {int(tempo_gasto)} segundos.")
                print("Você perdeu 5 pontos por demorar demais.")
                progresso["pontos"] = max(progresso["pontos"] - 5, 0)

            if verificar_resposta(exercicio['id'], resposta_usuario):
                print("Resposta correta! +10 pontos")
                progresso["pontos"] += 10
            else:
                print("Resposta incorreta. -1 vida")
                progresso["vidas"] -= 1

        if progresso["vidas"] <= 0:
            print("GAME OVER! Você perdeu todas as suas vidas!")
            break

        progresso = atualizar_nivel(progresso)
        salvar_progresso(progresso)


def abrir_loja(progresso):
    from loja import loja
    loja(progresso)
    salvar_progresso(progresso)

def menu():
    while True:
        opcao = input("\nJogo de Desafios de Física\n/start - Jogar\n/profile - Ver progresso\n/shop - Loja\n/sair - Sair do jogo\n>> ").strip().lower()
        if opcao == "/start":
            iniciar_jogo()
        elif opcao == "/profile":
            print(f"\nNível: {progresso['nivel']}, Pontos: {progresso['pontos']}, Vidas: {progresso['vidas']}, Pulos: {progresso['pulos']}, Dicas: {progresso['dicas']}")
        elif opcao == "/shop":
            abrir_loja(progresso)
        elif opcao == "/sair":
            print("Progresso salvo. Encerrando...")
            salvar_progresso(progresso, mostrar_mensagem=False)
            break
        else:
            print("Comando inválido!")

if __name__ == "__main__":
    try:
        menu()
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e.__class__.__name__}: {e}")