contNeg = 0
contPos = 0

for number in range(10):
    number = int(input("Digite um número: "))
    if number < 0:
        contNeg += 1
    else:
        contPos += 1
print(f"A quantidade de números negativos são: {contNeg}\n A quantidade de números positivos são: {contPos}")