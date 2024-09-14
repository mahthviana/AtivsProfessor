salarioMensal = str(input("Qual o seu salário mensal? \n"))
horasSemanaTrabalhadas = float(input("Quantas horas você trabalha semanalmente? \n"))

# CONVERTER STRING PARA UM FLOAT PARA PERMITIR CÁLCULOS (Porque tamo no brasil e a galera usa vírgula, não sei o por que esses gringo inventaram de usar um ponto)
salarioMensalFloat = salarioMensal.replace(",", ".")
salarioMensalFloat2 = float(salarioMensalFloat)

# HORAS TRABALHADAS NO MÊS
horasMesTrabalhadas = horasSemanaTrabalhadas * 4

# SALÁRIO POR HORA
salarioHora = salarioMensalFloat2 / horasMesTrabalhadas

print(f"Seu salário por hora trabalhada é de {salarioHora:.2f}")