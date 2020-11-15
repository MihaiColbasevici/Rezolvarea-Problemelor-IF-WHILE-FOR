n = int(input("Varsta lui Mihai: "))
if (n < 20):
    suma = 1
    dolari = 1
    for x in range(1, n + 1):
        dolari *= 2
        suma += dolari + x
    print("Mihai a primit $", suma)
    suma = 1
    dolari = 1
    for x in range(1, n + 1):
        dolari *= 2
        suma += dolari + x   
        if (suma > 100):
            print("La varsta de", x, "ani cadoul a fost mai mare de $100")