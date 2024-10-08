for i in range(1, 31):
    if i % 5 != 0:
        print(i)
    else:
        print(f"{i} é multiplo de 5")
    if i >= 20:
        break