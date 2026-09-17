n = int(input("digite um valor de n:"))

soma = 1
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
    soma += 1/fatorial

print(f"O resultado é: {soma}")
