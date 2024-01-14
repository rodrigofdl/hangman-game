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