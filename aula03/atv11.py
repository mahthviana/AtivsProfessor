numero = int(input("Digite um número entre 1 e 10: "))
while numero < 1 or numero > 10:
    numero = int(input("Número inválido. Digite um número entre 1 e 10: "))
    if numero >= 1 and numero <= 10:
        print(f"Você digitou o número {numero} e este é um número válido.")
        break