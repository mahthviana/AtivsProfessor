# Escreva um programa que solicite um número ao usuário e use
# um laço while para somar os dígitos do número até que a soma
# seja um único dígito.

numero = input("Digite um número: ")

while True:
    soma = 0
    for digito in str(numero):
        soma += int(digito)

    if soma < 10:
        break

    numero = soma

print(f"A soma dos dígitos até um único dígito é: {soma}")
    