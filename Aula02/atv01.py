idade1 = int(input("Digite uma idade: "))
idade2 = int(input("Digite uma idade: "))

if idade1 > idade2:
    print(f"A primeira idade {idade1} é maior que a idade {idade2}")
elif idade1 == idade2:
    print(f"A primeira idade {idade1} é igual a idade {idade2}")
else:
    print(f"A primeira idade {idade1} é menor que a idade {idade2}")