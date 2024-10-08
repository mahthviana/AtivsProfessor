# Crie um programa que solicite um número ao usuário e use um
# laço while para gerar e exibir a sequência de Collatz até chegar
# ao número 1.

numero = int(input("Digite um número: "))
print(numero)
while numero != 1:
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = 3 * numero + 1
    print(numero)