# Crie um programa que solicite dois números ao usuário,
# representando um intervalo. Use um laço while para exibir
# todos os números pares dentro desse intervalo.

num1 = int(input('Digite o primeiro número do intervalo: '))
num2 = int(input('Digite o segundo número do intervalo: '))

print(f'Os números pares no intervalo de {num1} a {num2} são: ')
while num1 <= num2:
    if num1 % 2 == 0:
        print(num1)
    num1 += 1
