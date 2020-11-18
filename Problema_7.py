n = int(input("Dati varsta lui Mihai: "))
if (n < 20):
    suma = 1
    dolari = 1
    for i in range(1, (n + 1)):
        dolari *= 2
        suma += (dolari + i)
    print("Mihai a primit $", suma)
    suma = 1
    dolari = 1
    for i in range(1, (n + 1)):
        dolari *= 2
        suma += (dolari + i)           
        if (suma > 100):
            print("Mihai avea", i, "ani cand a primit mai mult de $100")
            break
            
            