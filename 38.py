maior = None 
menor = None 

for i in range(100):
    valor = int(input("Digite um número inteiro: "))
    
    if maior is None or valor > maior:
        maior = valor
    if menor is None or valor < menor:
        menor = valor

print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")