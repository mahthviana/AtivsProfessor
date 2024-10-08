# Desenvolva um programa que solicite um número ao usuário
# e use um laço while para calcular o fatorial desse número.

cont = int(input('Digite um número que deseje saber o fatorial: ')) + 1
fatorial = 1
while cont > 1:
    cont -= 1
    print(cont)
    fatorial *= cont
print(f"o fatorial do número escolhido é {fatorial}")