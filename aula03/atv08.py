print("                 Menu de Cálculo de Notas:   ")
print("             1. Siga digitando as notas do aluno")
print(" 2. Quando digitado -1 o programa será encerrado automaticamente \n\n")

soma = 0
contador = 0

while True:
    nota = float(input("Digite a nota do aluno: "))
    
    if nota == -1:
        if contador > 0:
            media = soma / contador
            print(f"A média das notas é: {media:.2f}")
        else:
            print("Nenhuma nota foi digitada.")
        break
    elif nota < -1:
        print("Nota inválida. Digite uma nota válida (ou -1 para encerrar o programa).")
    else:
        soma += nota
        contador += 1
