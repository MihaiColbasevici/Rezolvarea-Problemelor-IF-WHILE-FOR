n = int(input("Dati un numar: "))
if (n == 28) or (n == 29):
    print("Februarie")
elif (n == 30):
    print("Aprilie, Iunie, Septembrie, Noiembrie")
elif (n == 31):
    print("Ianuarie, Martie, Mai, Iulie, August, Octombrie, Decembrie")
else:
    print("Alegeti alt numar")
