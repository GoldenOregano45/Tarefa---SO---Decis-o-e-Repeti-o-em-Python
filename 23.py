print ("digite em ordem crescente menos o ultimo numero ele tem q ser aleatorio")
a= float(input("digite o 1 numero:"))
b= float(input("digite o 2 numero:"))
c= float(input("digite o 3 numero:"))
d= float(input("digite o 4 numero:"))

if d < a:
    resultado = [d, a, b, c]
elif d < b:
    resultado = [a, d, b, c]
elif d < c:
    resultado = [a, b, d, c]
else:
    resultado = [a, b, c, d] 
print ("ordem crescente:" , resultado)