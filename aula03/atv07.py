numero = int(input("Digite o número que deseja fazer a multiplicação: \n"))
cont = 0
while cont < 10:
    cont += 1
    multiplica = numero*cont
    if multiplica % 3 == 0:
        print(multiplica)