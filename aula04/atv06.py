soma = 0

for number in range(1, 51):
    if number % 2 == 0:
        soma += number
        print(f"{number} \n+")
    else:
        continue
print(f"=\n{soma}")