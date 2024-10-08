palavra = str(input("Digite uma palavra e eu direi quantas vogais tem: "))
cont = 0
for caracter in palavra:
    if caracter.lower() in "aeiou":
        cont += 1
print(f"a palavra {palavra.capitalize()} tem {cont} vogais")