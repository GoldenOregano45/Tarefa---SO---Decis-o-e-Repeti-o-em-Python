n1= float(input("nota 1: "))
n2= float(input("nota 2: "))
n3= float(input("nota 3: "))
n4= float(input("nota 4: "))

media = (n1+n2+n3+n4)/4
if media >= 6:
    situacao = "aprovado"
elif media >= 3:
    situacao = "recuperação"
else:
    situacao = "reprovado"

print(f"{situacao} ")
print(f"média: {media}")
