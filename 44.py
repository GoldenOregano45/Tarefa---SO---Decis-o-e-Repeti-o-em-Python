base = float(input("digite a base:"))
expoente = int(input("digite o expoente:"))

resultado = 1 
for i in range(expoente):
    resultado *=base

print(f"{base} elevado a {expoente} = {resultado} ")