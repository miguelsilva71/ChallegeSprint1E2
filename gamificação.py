# Sistema de Gamificação Sustentável SoulUp com Avatar


acoes = ("Reciclagem", "Transporte Público ", "Economia de Energia", "Economia de Água", "Bicicleta",
         "Plantio de Árvore", "Banho Rápido")

pontos_ecoa = 0
pontos_resgatados = 0
historico = []


def identificar_nivel():
    if pontos_ecoa < 100:
        return "Semente"
    elif pontos_ecoa < 300:
        return "Broto"
    elif pontos_ecoa < 600:
        return "Árvore"
    else:
        return "Expert"


def mostrar_menu():
    nivel = identificar_nivel()
    print("\n=== DASHBOARD SOULUP ===")
    print(f"[ Pontos Disponíveis: {pontos_ecoa} | Já Resgatados: {pontos_resgatados} | Nível: {nivel} ]")
    print("---------------------------------------------------------------------------")
    print("1 - Registrar ação sustentável")
    print("2 - Ver Meu Nível e Estatísticas")
    print("3 - Resgatar Recompensas (Benefícios Reais)")
    print("4 - Sugestão do Avatar")
    print("5 - Ver Ranking da Semana ")
    print("6 - Sair")


def registrar_acao():
    global pontos_ecoa
    print("\nAções Sustentáveis disponíveis:")

    for i, acao in enumerate(acoes):
        print(f"{i + 1} - {acao}")

    try:
        escolha = int(input("\nQual ação sustentável você realizou hoje? "))
        if 1 <= escolha <= len(acoes):
            acao_escolhida = acoes[escolha - 1]

            pontos = calcular_pontos(acao_escolhida)
            pontos_ecoa += pontos
            historico.append(acao_escolhida)

            print(f"Boa! Você ganhou +{pontos} Pontos ECOA com: {acao_escolhida}!")
            print("Transação validada e registrada com sucesso via Blockchain.")
        else:
            print("Opção inválida!")
    except ValueError:
        print("Digite um número válido!")


def calcular_pontos(acao):
    if acao == "Reciclagem":
        return 30
    elif acao == "Transporte Público":
        return 50
    elif acao == "Economia de Energia":
        return 20
    elif acao == "Economia de Água ":
        return 15
    elif acao == "Bicicleta":
        return 25
    elif acao == "Plantio de Árvore":
        return 100
    elif acao == "Banho Rápido":
        return 20
    else:
        return 10


def ver_meu_nivel():
    nivel = identificar_nivel()
    print(f"\n--- SEU NÍVEL ATUAL: {nivel} ---")
    print(f"Saldo Disponível: {pontos_ecoa} Pontos ECOA")
    print(f"Total já Resgatado: {pontos_resgatados} Pontos ECOA")
    print(f"Histórico de Missões: {historico}")

    if nivel == "Semente 🌱":
        print(f"Progresso: Faltam {100 - pontos_ecoa} pontos para evoluir para Broto!")
    elif nivel == "Broto 🌿":
        print(f"Progresso: Faltam {300 - pontos_ecoa} pontos para evoluir para Árvore!")
    elif nivel == "Árvore 🌳":
        print(f"Progresso: Faltam {600 - pontos_ecoa} pontos para evoluir para Expert!")


def resgatar_recompensas():
    global pontos_ecoa, pontos_resgatados
    print("\n=== VITRINE DE RECOMPENSAS SOULUP ===")
    print("1 - Plantar 1 Árvore ------------ 200 pontos")
    print("2 - Kit Reciclagem -------------- 250 pontos")
    print("3 - Crédito Transporte ---------- 300 pontos")
    print("4 - Cupom Mercado Orgânico ------ 350 pontos")
    print("5 - Aluguel de Bicicleta -------- 400 pontos")
    print("6 - Desconto na Energia --------- 500 pontos")
    print("7 - Adotar uma Área Verde ------- 1500 pontos")
    print("8 - Mês de Energia Grátis ------- 2000 pontos")
    print("9 - Voltar")

    try:
        opcao_troca = int(input(f"\nSeu Saldo: {pontos_ecoa} pts. Escolha um benefício: "))

        custo = 0
        recompensa = ""

        if opcao_troca == 1:
            custo = 200
            recompensa = "Plantar 1 Árvore"
        elif opcao_troca == 2:
            custo = 250
            recompensa = "Kit Reciclagem"
        elif opcao_troca == 3:
            custo = 300
            recompensa = "Crédito Transporte (R$ 20)"
        elif opcao_troca == 4:
            custo = 350
            recompensa = "Cupom Mercado Orgânico (R$ 30)"
        elif opcao_troca == 5:
            custo = 400
            recompensa = "Aluguel de Bicicleta (1 semana grátis)"
        elif opcao_troca == 6:
            custo = 500
            recompensa = "Desconto na Energia (10% na fatura)"
        elif opcao_troca == 7:
            custo = 1500
            recompensa = "Adotar uma Área Verde (Parque por 1 mês)"
        elif opcao_troca == 8:
            custo = 2000
            recompensa = "Mês de Energia Grátis"
        elif opcao_troca == 9:
            return
        else:
            print("Opção inválida!")
            return

        if pontos_ecoa >= custo:
            pontos_ecoa -= custo
            pontos_resgatados += custo
            print(f"\n Sucesso! Você resgatou: {recompensa}!")
            print(f"Foram utilizados {custo} Pontos ECOA.")
        else:
            print(f"\n Pontos insuficientes! Você precisa de {custo} pontos, mas tem apenas {pontos_ecoa}.")

    except ValueError:
        print("Entrada inválida!")


def sugestao_avatar():
    nivel = identificar_nivel()
    print(f"\n--- MENSAGEM DO AVATAR ---")
    if nivel == "Semente":
        print("Avatar: Que ótimo ver você por aqui! Registre missões diárias para fazermos nossa semente brotar.")
    elif nivel == "Broto":
        print("Avatar: Crescendo firme! Junte 200 pontos para resgatar 'Plantar 1 Árvore' na aba de Recompensas!")
    else:
        print(
            f"Avatar: Parabéns pelo nível {nivel}! Continue acumulando pontos para desbloquear recompensas avançadas.")



def ver_ranking():
    competidores = [
        {"nome": "Ana", "pontos": 350},
        {"nome": "Carlos", "pontos": 280},
        {"nome": "Você", "pontos": pontos_ecoa},
        {"nome": "Marina", "pontos": 150},
        {"nome": "Pedro", "pontos": 120}
    ]


    competidores_ordenados = sorted(competidores, key=lambda x: x['pontos'], reverse=True)

    print("\n==============================")
    print("      RANKING DA SEMANA       ")
    print("==============================")


    for indice, usuario in enumerate(competidores_ordenados):
        posicao = indice + 1
        nome = usuario['nome']
        pontos = usuario['pontos']


        if nome == "Você":
            print(f"-> {posicao}º {nome:<10} | {pontos} pts * (Sua posição)")
        else:
            print(f"   {posicao}º {nome:<10} | {pontos} pts")
    print("==============================")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha: ")

        match opcao:
            case "1":
                registrar_acao()
            case "2":
                ver_meu_nivel()
            case "3":
                resgatar_recompensas()
            case "4":
                sugestao_avatar()
            case "5":
                ver_ranking()
            case "6":
                print("Saindo... Seus dados de impacto social foram salvos com segurança na Web 3.0.")
                break
            case _:
                print("Opção inválida! Digite de 1 a 6.")


if __name__ == "__main__":
    main()