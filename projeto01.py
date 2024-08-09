import random

naipes = ['♦', '♠', '♥', '♣']
numeros = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']
valores = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'J': 10,
    'Q': 10,
    'K': 10
}

def criar_baralho():
    """Cria um baralho de cartas."""
    return [f'{numero} {naipe}' for naipe in naipes for numero in numeros]

def calcular_pontos(cartas_jogador):
    """Calcula a pontuação do jogador com base nas cartas na mão."""
    pontos = 0
    ases = 0
    for carta in cartas_jogador:
        numero = carta.split()[0]
        pontos += valores[numero]
        if numero == 'A':
            ases += 1
    # Ajustar os pontos se houver ases e o total ultrapassar 21
    while pontos + 10 <= 21 and ases:
        pontos += 10
        ases -= 1
    return pontos

def mostrar_menu(pontos):
    """Exibe o menu principal do jogo."""
    print("\nMenu:")
    print('====================================')
    print("1 - Pegar carta")
    print("2 - Parar")
    print("3 - Ver pontos")
    print('====================================')
    print()
    print(f'Pontos: {pontos}')
    print()

def pegar_carta(cartas_disponiveis, mao_jogador):
    """Pega uma carta do baralho e atualiza a mão do jogador."""
    if not cartas_disponiveis:
        print("O baralho acabou. Não há mais cartas para pegar.")
        return
    carta = cartas_disponiveis.pop()
    mao_jogador.append(carta)
    valor = valores[carta.split()[0]]
    return carta, valor

def jogo_blackjack():
    """Função principal do jogo Black Jack."""
    cartas_disponiveis = criar_baralho()
    random.shuffle(cartas_disponiveis)
    mao_jogador = []
    pontos = 0

    while True:
        mostrar_menu(pontos)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            carta, valor = pegar_carta(cartas_disponiveis, mao_jogador)
            if carta:
                pontos = calcular_pontos(mao_jogador)
                print(f'Você pegou: {carta} - Valor: {valor}')
                if pontos > 21:
                    print("Você ultrapassou 21 pontos. Você perdeu!")
                    break

        elif opcao == '2':
            print("Você parou.")
            print(f'Seu total de pontos: {pontos}')
            break

        elif opcao == '3':
            print(f'Seu total de pontos: {pontos}')

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    while True:
        jogo_blackjack()
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            break
