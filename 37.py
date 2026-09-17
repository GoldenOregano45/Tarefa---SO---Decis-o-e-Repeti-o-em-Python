n = int((input ("digite quantos termos vc deseja criar:")))

a,b = 0,1 
print(("serie de fibonacci:"))
for _ in  range(n):
    print(a, end="")
    a,b = b, a + b 
print()