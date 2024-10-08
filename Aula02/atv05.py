prod = str(input("Digite o nome do produto: \n"))
precProd = float(input("Digite o Valor do produto para tê-lo com 5% de desconto: \n"))
desc = (precProd * 5) / 100
precProd -= desc

print(f"O produto {prod} de valor {precProd + desc:.2f} com 5% de desconto fica com {precProd:.2f}")