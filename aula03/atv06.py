numero = 0
soma = 0

while numero >= 0:
    numero = float(input("Digite um número: "))
    if numero < 0:
        print(soma)
        break
    soma += numero
    print(soma)