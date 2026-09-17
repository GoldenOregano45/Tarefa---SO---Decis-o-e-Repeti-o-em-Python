n = int(input("digite um numero:"))

if n % 2 == 0 and n % 3 == 0:
    print("o numero é divisivel por 2 e 3")
elif n % 2 == 0:
    print("o numero é divisivel por 2")
elif n % 3 == 0:
    print("o numero é divisivel por 3")
else:
    print("esse numero nao e divisivel por 2 e 3")