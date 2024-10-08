numero = int(input("Digite um número que deseje que haja uma contagem: \n"))
cont = 0
while cont < numero:
    cont += 1
    if cont % 2 != 0:
        print(cont)