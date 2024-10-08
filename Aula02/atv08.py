frase = str(input("Digite uma frase: \n"))
palavra = str(input("Digite uma palavra para verificar se ela existe na frase: \n"))

if palavra in frase: 
    print("Show, meu chapa, essa palavra tem na tua frase.")
else: 
    print("Tem essa palavra não.")