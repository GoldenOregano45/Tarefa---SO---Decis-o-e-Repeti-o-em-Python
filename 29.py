tipo = int(input("digite o tipo de investimento: 1- Poupança, 2- Renda Fixa,"))
valor = float(input("digite o valor do investimento:"))

if tipo == 1:
    valor_corrido = valor * 1.03
    print(f"o valor corrigido da poupança é: {valor_corrido:.2f}")
elif tipo == 2:
    valor_corrido = valor * 1.05
    print(f"o valor corrigido da renda fixa é: {valor_corrido:.2f}")
else:
    print("Tipo de investimento inválido.")