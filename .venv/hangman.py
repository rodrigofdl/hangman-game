# Importações
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Função para escolher palavra aleatória
def palavra_aleatoria():
    lista_de_palavras = ["abacate", "banana", "morango", "uva", "laranja", "maca", "pera"]
    return random.choice(lista_de_palavras)

# Função para exibir a palavra oculta
def exibir_palavra_oculta(palavra, letras_corretas):
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    return palavra_oculta

# Exibir tentativas restantes
def exibir_tentativas_restantes(tentativas):
    print("Tentativas restantes: ", tentativas)

# Função para receber a letra do jogador
def receber_letra():
    return input("Digite uma letra: ").lower()

# Função principal do jogo
def jogo_da_forca():
    limpa_tela()
    palavra_secreta = palavra_aleatoria()
    letras_corretas = []
    tentativas_restantes = 6

    while tentativas_restantes > 0:
        palavra_oculta = exibir_palavra_oculta(palavra_secreta, letras_corretas)
        print(palavra_oculta)
        exibir_tentativas_restantes(tentativas_restantes)
        letra_digitada = receber_letra()

        if letra_digitada in letras_corretas:
            print("Essa letra já foi tentada! Tente novamente.")
            continue

        if letra_digitada in palavra_secreta:
            letras_corretas.append(letra_digitada)
            if all(letra in letras_corretas for letra in palavra_secreta):
                print("Parabens! Você venceu. A palavra é:", palavra_secreta)
                break

        if letra_digitada == palavra_secreta:
            print("Parabens! Você venceu. A palavra é:", palavra_secreta)
            break

        else:
            tentativas_restantes -= 1

        if tentativas_restantes == 0:
            print("Você perdeu! A palavra correta era:", palavra_secreta)

# Iniciar jogo
jogo_da_forca()