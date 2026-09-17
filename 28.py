venda = float(input("Digite o valor da venda: "))
preco_atual = float(input("Digite o preço de atual :"))

if venda <500 and preco_atual < 30.00:
    novo_preco = preco_atual * 1.10
elif 500 <= venda <= 1000 and 30.00 <= preco_atual < 80.00:
    novo_preco = preco_atual * 1.15
elif venda > 1000 and preco_atual >= 80.00:
    novo_preco = preco_atual * 0.95
else:
    novo_preco = preco_atual
print(f"O novo preço do produto é: R$ {novo_preco:.2f}")