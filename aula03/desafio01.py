# Crie um programa que use um laço while para somar
# todos os números pares de 1 a 100 e exiba o resultado.

cont = 0
soma = 0
while cont <= 100:
    cont += 1
    if cont % 2 == 0:
        print(f"A soma dos números pares de 1 a 100 é: {soma}")
        soma += cont
