# Desenvolva um jogo de adivinhação onde o
# programa escolhe um número aleatório entre 1 e
# 100. O usuário deve tentar adivinhar o número, e
# o programa deve fornecer dicas se o palpite está
# muito alto ou baixo.

import random

print("Este é um jogo de adivinhação! Será que você consegue?")
print("Regra:\n1. você tem infinitas chances até acertar o número que vai de 1 a 100!")
numero = int(random.randint(1, 100))

while True:
    palpite = int(input("Digite seu palpite: "))
    
    if palpite < numero:
        print("O seu palpite é menor que o número escolhido... Tente novamente")
    elif palpite > numero:
        print("O seu palpite é maior que o número escolhido... Tente novamente")
    else:
        print("Você acertou!!!!")
        break