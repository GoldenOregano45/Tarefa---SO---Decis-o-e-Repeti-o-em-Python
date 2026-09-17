a = int(input("digite o 1 numero:"))
b = int(input("digite o 2 numero:"))

menor = min(a, b)
maior = max(a, b)

soma = 0
for i in range(menor, maior + 1):
    if i % 2 != 0:
        soma += i

print(f"O maior numero e {maior}")
print(f"a soma dos numeros impares entre {menor} e {maior} é: {soma}")