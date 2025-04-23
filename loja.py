def loja(progresso):
    while True:
        print("\nLoja de Melhorias:")
        print(f"Pontos disponíveis: {progresso['pontos']}")
        print("1. Comprar Pulo (40 pontos)")
        print("2. Comprar Dica (20 pontos)")
        print("3. Sair da Loja")

        escolha = input("\nEscolha uma opção: ").strip()

        if escolha == "1" and progresso["pontos"] >= 40:
            progresso["pontos"] -= 40
            progresso["pulos"] += 1
            print("Você comprou um Pulo!")
        elif escolha == "2" and progresso["pontos"] >= 20:
            progresso["pontos"] -= 20
            progresso["dicas"] += 1
            print("Você comprou uma dica! Ela poderá ser usada durante uma pergunta digitando /dica.")
        elif escolha == "3":
            break
        else:
            print("Opção inválida ou pontos insuficientes!")



            