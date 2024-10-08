senha = '1369751357'
cont = 3

login = input("Digite sua senha: ")

while cont > 0:
    if login == senha:
        print("Acesso permitido.")
        break
    else:
        cont -= 1
        if cont > 0:
            print("Senha incorreta. Tente novamente.")
            login = input("Digite sua senha: ")
        else:
            print("Acesso negado.")
