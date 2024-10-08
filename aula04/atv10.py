for num in range(1, 11):
    numero = int(input("Digite um número positivo ou negativo: "))
    if numero > 0:
        print(f"{numero} é positivo")
    elif numero < 0:
        print(f"{numero} é negativo")
    else:
        print("Programa Encerrado...")
        break