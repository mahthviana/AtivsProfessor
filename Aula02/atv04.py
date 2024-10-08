nota1 = float(input("Digite a primeira nota do aluno: \n"))
nota2 = float(input("Digite a segunda nota do aluno: \n"))

if nota1 >= 6 and nota2 >= 6:
    print("As duas notas são iguais ou maiores que 6")
elif nota1 >= 6 and nota2 < 6:
    print("A primeira nota é igual ou maior que 6 e a segunda nota é menor que 6 ")
elif nota1 < 6 and nota2 >= 6:
    print("A primeira nota é menor que 6 e a segunda nota é igual ou maior que 6 ")
else: 
    print("As duas notas são menores que 6")