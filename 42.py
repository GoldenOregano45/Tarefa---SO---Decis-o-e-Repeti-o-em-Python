soma = 0 
for i in range(1, 51):
    numerador = 1
    denominador = 2 * i-1
    soma += numerador / denominador

print(f"O resultado da serie é: {soma}")