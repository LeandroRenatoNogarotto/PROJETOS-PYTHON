branco = " "
token = ["X", "O"]
def criarTabuleiro():
    tabuleiro = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ] #cria tabuleiro inicial
    return tabuleiro #retorna tabuleiro


def printTabueliro(tabuleiro): #imprime tabauleiro

    for i in range(3):
        print(" ", end="")
        print(" |".join(tabuleiro[i])) #imprime simbolo caso seja ocupado
        if (i < 2):
            print(" --------")


def validainput(mensagem):
    try:
        n = int(input(mensagem))
        if (n >= 1 and n <= 3): #caso numero seja valido
            return n - 1
        else:
            print("Numero precisa estar entre 1 e 3")
            return validainput(mensagem) #retorna para redigitação
    except:
        print("Numero nao valido")
        return validainput(mensagem) #retorna para redigitação


def verificaMovimento(tabuleiro, i, j): #verifica se espaço está ocupado
    if (tabuleiro[i][j] == branco):
        return True
    else:
        return False


def fazMovimento(board, i, j, jogador): #prenche espaço que posteriormente será impresso
    board[i][j] = token[jogador]


def verificaGanhador(tabuleiro): #verifica se caso alguma das condições de vitoria foi atendida

    # linhas
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != branco):
            return tabuleiro[i][0]

    # coluna
    for i in range(3):
        if (tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != branco):
            return tabuleiro[0][i]

    # diagonal principal
    if (tabuleiro[0][0] != branco and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]):
        return tabuleiro[0][0]

    # diagonal secundaria
    if (tabuleiro[0][2] != branco and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]):
        return tabuleiro[0][2]

    for i in range(3):
        for j in range(3):
            if (tabuleiro[i][j] == branco):
                return False

    return "EMPATE" #caso nenhuma das condições foi atendida o jogo termina em empate

jogador = 0  #jogador 1
tabuleiro = criarTabuleiro()
ganhador = verificaGanhador(tabuleiro)
print(f"JOGADOR:{jogador+1}")
while (not ganhador):
    printTabueliro(tabuleiro)
    print("::::::::::::\n")
    i = validainput("Digite a linha: ")
    j = validainput("Digite a coluna: ")
    if (verificaMovimento(tabuleiro, i, j)):
        fazMovimento(tabuleiro, i, j, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("A posicao informado ja esta ocupada")

    ganhador = verificaGanhador(tabuleiro)
    print(f"JOGADOR:{jogador + 1}")

print("::::::::::::\n")
printTabueliro(tabuleiro)
print("Ganhador = ", ganhador)
print("===================")
