#Autor: Marco


import random

PASS_MARK = 60


def leia_float(prompt, minimo=0.0, maximo=100.0):
    while True:
        try:
            valor = float(input(prompt).replace(",", "."))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um valor entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida. Use apenas números.")


def calcula_media_ponderada(avaliacoes):
    soma_pesos = sum(peso for _, peso in avaliacoes)
    if soma_pesos == 0:
        return 0.0
    soma_notas = sum(nota * peso for nota, peso in avaliacoes)
    return soma_notas / soma_pesos


def modo_maligno(media_atual):
    print("\nModo Maligno ativado! A noite está escura e as notas tremem...")
    if media_atual >= PASS_MARK:
        print("Você já escapou da reprovação, mas o mal não descansa.")
        melhora = max(0.0, min(100.0 - media_atual, random.uniform(1.0, 5.0)))
        nova_media = media_atual + melhora
        print(f"Curva sombria adicionou +{melhora:.1f} pontos à média. Nova média: {nova_media:.1f}")
        return nova_media

    deficit = PASS_MARK - media_atual
    print(f"Sua média atual é {media_atual:.1f}. O abismo da reprovação está a {deficit:.1f} pontos.")
    print("O mal oferece um pacto: um salto sombrio de esperança..."
          " Mas cuidado, ele custa suspense e nervos.")
    bonus = min(100.0 - media_atual, max(0.0, random.uniform(deficit * 0.7, deficit * 1.3)))
    nova_media = media_atual + bonus
    if nova_media >= PASS_MARK:
        print(f"A curva maligna funciona! Nova média: {nova_media:.1f}. Você escapou da reprovação... por agora.")
    else:
        print(f"A maldade falhou um pouco. Nova média: {nova_media:.1f}. Ainda precisa de {PASS_MARK - nova_media:.1f} pontos.")
    return nova_media


def calcula_media_virtual():
    print("\nVamos montar sua nota maligna. Quantas avaliações você quer usar?")
    quantidade = int(leia_float("Digite o número de avaliações (2-10): ", minimo=2, maximo=10))
    avaliacoes = []
    for i in range(1, quantidade + 1):
        nota = leia_float(f"Nota da avaliação {i} (0-100): ")
        peso = leia_float(f"Peso da avaliação {i} (1-10): ", minimo=1, maximo=10)
        avaliacoes.append((nota, peso))
    media = calcula_media_ponderada(avaliacoes)
    print(f"\nSua média ponderada é: {media:.1f}")
    return media


def mostra_status(media):
    if media >= PASS_MARK:
        print("Status: APROVADO! Que seja um triunfo maligno...")
    else:
        print("Status: REPROVADO. O terror das notas continua presente.")


def menu():
    print("\n=== CALCULADORA DE NOTA MALIGNA ===")
    print("1 - Calcular média escolar")
    print("2 - Calcular média e acionar modo maligno")
    print("3 - Sair")
    return input("Escolha uma opção: ").strip()


def main():
    while True:
        opcao = menu()
        if opcao == "1":
            media = calcula_media_virtual()
            mostra_status(media)
        elif opcao == "2":
            media = calcula_media_virtual()
            mostra_status(media)
            media_maligna = modo_maligno(media)
            mostra_status(media_maligna)
        elif opcao == "3":
            print("Saindo... que a maldade deixe apenas os suspense.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
