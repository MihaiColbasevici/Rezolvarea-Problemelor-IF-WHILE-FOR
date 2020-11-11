n = int(input("Dati un numar: "))
factorial = 1
suma = 0
for n in range(1, n):
    factorial *= n
    suma += factorial
print(suma)