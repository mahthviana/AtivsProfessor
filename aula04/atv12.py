soma = 0
for i in range(1, 6):
    preco = float(input(f"Digite o preco do produto{i}: "))
    soma += preco
    if soma > 100:
        desconto = soma - ((10 * soma ) / 100)
        print(f"O total com 10% de desconto será de R${desconto} de desconto")
        break