frase = str(input("Digite uma frase: \n"))
caracter = str(input("Digite um caracter para verificar se ele existe na frase: \n"))

if caracter in frase: 
    print("Show, meu chapa, essa letra tem na tua frase.")
else: 
    print("Tem essa letra não.")