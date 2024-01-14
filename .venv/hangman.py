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
