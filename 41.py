print ("combinaçoes de 2 dados cuja soma seja 7")
for dado in range (1,7):
    for dado2 in range (1,7):
        if dado + dado2 == 7:
            print (f"{dado} + {dado2} = 7")