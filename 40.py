a = int(input("digite o  primeiro numero:"))
b = int(input("digite o segundo numero:"))

manor = min(a, b)
maior = max(a, b)

print("numeros primos encontrados:")
for n in range(manor, maior + 1):
    if n < 2:
        continue
    primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(n, end =" ")
print()