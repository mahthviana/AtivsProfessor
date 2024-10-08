usuario = "admin"
senha = "1234"

loginUsuario = str(input("Usuário: "))
loginSenha = str(input("Senha: "))

if loginUsuario == usuario and loginSenha == senha:
    print("Login efetuado com sucesso!")
else: 
    print("Usuário ou Senha inválidos")