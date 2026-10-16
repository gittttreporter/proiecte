a = int(input("Introdu primul numar: "))
b = int(input("Introdu al doilea numar: "))
if a > 1000000000 or b > 1000000000:
    print("Nu se poate! Numere prea mari!")
else:
    print(a + b)