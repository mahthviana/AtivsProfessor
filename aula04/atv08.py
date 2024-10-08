cont = 0
soma = 0

for notasAluno in range(5):
    notas = float(input("Dgite a nota do aluno: "))
    soma += notas
    cont += 1
    if cont >= 5:
        media = soma / cont
        break
if media >= 6:
    print(f"Aluno foi aprovado com nota {media:.1f}!!!")
else:
    print(f"Aluno foi reprovado com nota {media:.1f}!")
