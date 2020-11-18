n = int(input("Dati numarul n (puterea): "))
m = int(input("Dati numarul m (baza): "))
exp = 0
rasp = ''
nu = ''
if (n < m):
    print("Dati alte numere.")
if (m < n):
  for i in range(1, n):
    exp=m ** i
    if (exp == n):
      rasp = 'Da'
    else:
      nu = 'Nu'
  if (rasp == 'Da'):
    print(rasp)
  else:
    print('Nu')