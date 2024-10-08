# Faça um programa que use um laço while para exibir os
# primeiros 20 termos da sequência de Fibonacci. 

cont = 0
termo1 = 0
termo2 = 0
while cont < 20:
    cont += 1
    if cont == 1:
        termo1 = 1
        print(termo1)
    elif cont == 2:
        termo2 = 1
        print(termo2)
    else:
        termo3 = termo1 + termo2
        print(termo3)
        termo1 = termo2
        termo2 = termo3