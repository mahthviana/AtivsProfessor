print("Caso você tenha atingido a quantidade de 10 unidades do produto que deseja comprar, \nvocê terá 10% de desconto na sua compra\n")

produto = str(input("Digite o número do produto: \n"))
qntd = float(input(f"Digite a quantidade que você deseja comprar de {produto}: \n"))
preco = float(input("Digite o valor original do produto: \n"))

if qntd >= 10:
    precoTotal = preco * qntd 
    desconto = precoTotal - ((precoTotal * 10) / 100) 
    print(f"Devido a quantidade de produtos ser igual ou superior a 10, você receberá 10% de desconto\nO valor de R${precoTotal:.2f} sairá por R${desconto}")
else:
    print("Devido ao seu produto não ter chegado a um total de 10 unidades, não será possível atribuir um desconto.")