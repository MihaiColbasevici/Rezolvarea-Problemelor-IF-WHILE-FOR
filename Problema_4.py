num1, nim1 = input("Dati o fractie (exemplu: 2/3): ").split('/')
num2, nim2 = input("Dati o alta fractie (exemplu: 2/3): ").split('/')
num1 = int(num1)
nim1 = int(nim1)
num2 = int(num2)
nim2 = int(nim2)
if (nim1 == nim2):
    if ((num1 + num2) == nim1):
        print(num1, "/", nim1, " + ", num2, "/", nim2, " = 1")
    if ((num1 + num2) < nim1):
        a = num1 + num2
        b = nim1
        r = a % b
        while r:
            a = b
            b = r
            r = a % b
        numarators = (num1 + num2) / b
        numitors = nim1 / b
        print(num1, "/", nim1, " + ", num2, "/", nim2, " = ", int(numarators), "/", int(numitors))
    if ((num1 + num2) > nim1):
        numarator = num1 + num2
        numitor = nim1
        intreg = numarator // numitor
        rest = numarator - (intreg * numitor)
        if (rest == 0):
            print(num1, "/", nim1, " + ", num2, "/", nim2, " = ", intreg)
        elif (rest != 0):
            a = rest
            b = numitor
            r = a % b
            while r:
                a = b
                b = r
                r = a % b
            rests = rest / b
            numitors = numitor / b
            print(num1, "/", nim1, " + ", num2, "/", nim2, " = ", intreg, "intreg", int(rests), "/", int(numitors))
if (nim1 != nim2):
    numitor = nim1 * nim2
    numarator = (num1 * nim2) + (num2 * nim1)
    if ((num1 + num2) < nim1):
        a = numarator
        b = numitor
        r = a % b
        while r:
            a = b
            b = r
            r = a % b
        numarators = numarator / b
        numitors = numitor / b
        print(num1, "/", nim1, " + ", num2, "/", nim2, " = ", int(numarators), "/", int(numitors))
    if ((num1 + num2) > nim1):
        intreg = numarator // numitor
        rest = numarator - (intreg * numitor)
        a = rest
        b = numitor
        r = a % b
        while r:
            a = b
            b = r
            r = a % b
        rests = rest / b
        numitors = numitor / b
        print(num1, "/", nim1, " + ", num2, "/", nim2, " = ", intreg, "intreg", int(rests), "/", int(numitors))

# inmultirea
numarator_inm = num1 * num2
numitor_inm = nim1 * nim2
if (numarator_inm < numitor_inm):
    a = numarator_inm
    b = numitor_inm
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    numarator_inms = numarator_inm / b
    numitor_inms = numitor_inm / b
    print(num1, "/", nim1, " * ", num2, "/", nim2, " = ", int(numarator_inms), "/", int(numitor_inms))
if (numarator_inm > numitor_inm):
    intreg_inm = numarator_inm // numitor_inm
    rest_inm = numarator_inm - (intreg_inm * numitor_inm)
    a = rest_inm
    b = numitor_inm
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    rest_inms = rest_inm / b
    numitor_inms = numitor_inm / b
    print(num1, "/", nim1, " * ", num2, "/", nim2, " = ", intreg_inm, "intreg", int(rest_inms), "/", int(numitor_inms))