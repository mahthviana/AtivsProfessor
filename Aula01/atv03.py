nomeDoAluno = str(input("Digite o nome do aluno: ")).capitalize()
nomeDaMateria = str(input("Digite o nome da matéria: ")).capitalize()

nota1 = float(input("\n\nDigite a primeira nota do aluno aqui: "))
nota2 = float(input("Digite a segunda nota do aluno aqui: "))
nota3 = float(input("Digite a terceira nota do aluno aqui: "))
nota4 = float(input("Digite a quarta nota do aluno aqui: "))

mediaDoAluno = (nota1 + nota2 + nota3 + nota4) / 4

print(f"\n\nA média do aluno {nomeDoAluno} na matéria {nomeDaMateria} é {mediaDoAluno:.1f}")