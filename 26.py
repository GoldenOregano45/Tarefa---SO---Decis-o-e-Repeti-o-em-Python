a = int(input("digite o 1 numero:"))
b = int(input("digite o 2 numero:"))

maior =max(a, b)
menor = min(a, b)

if maior % menor == 0:
    print ("o maior é divisivel pelo menor" )
else:
    print ("o maior não é divisivel pelo menor" )