import math

a= float(input("digite a coeficiente 1 numero:"))
b= float(input("digite a coeficiente 2 numero:"))
c= float(input("digite a coeficiente 3 numero:"))

delta = b**2 - 4*a*c
if delta < 0:
    print("não existe raiz real")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("as raízes sao")
    print(f"{x1}")
    print(f"{x2}")