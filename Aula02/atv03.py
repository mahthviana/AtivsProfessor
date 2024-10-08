idade = int(input("Digite sua idade: "))
verHabi = int(input("Você tem habilitação (1. Sim\n2. Não): "))

if idade >= 18 and verHabi == 1:
    print("Você pode dirigir!")
elif idade < 18:
    print("Você é menor de idade e não pode dirigir!")
else:
    print("Você é maior de idade, porém não tem habilitação e nã pode dirigir! ")