# Faça um programa que use um laço while para fazer uma
# contagem regressiva de um número inserido pelo usuário até 0.
# Durante a contagem, exiba "Número par" para os números
# pares.

cont = int(input("Digite um número que seja o marco inicial da contagem regressiva: "))

while cont >= 0: 

    if cont % 2 == 0:
        print(f"{cont} É número par")
    elif cont % 2 != 0:
        print(cont)
    cont -= 1