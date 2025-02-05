def ticket(buy, tot):
    tot=tot-buy
    print("Biglietti rimasti: ", tot)
    return tot

tot=100
k=0
while (tot>0):
    k += 1
    if (tot>3):
        buy=int(input("Quanti biglietti si vogliono acquistare? (max 4): "))
        tot=ticket(buy, tot)
    else:
        buy=int(input("Quanti biglietti si vogliono acquistare? (max %d): " %(tot)))
        tot=ticket(buy, tot)
print("\nNumero di acquirenti: ", k)
