nome = str(input("Digite seu nome: \n")).capitalize()
idade = int(input("Digite sua idade: \n"))
altura = float(input("Digite sua altura (Apenas números): \n"))

calcAltura = altura / 100

print(f"Seu nome é {nome} {type(nome)} \nSua idade é {idade} {type(idade)} \nSua altura é {calcAltura:.2f} {type(altura)}")