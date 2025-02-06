carte = 45
n_pile = 5
pile = []
refer = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pile.append(20)
pile.append(5)
pile.append(1)
pile.append(9)
pile.append(10)

print(pile)
c = 0
while pile!=refer:
    c += 1
    j = []
    elim = False
    for i in range(len(pile)):
        pile[i] -= 1
        if pile[i]==0:
            j.append(i)
            elim = True
    pile.append(i+1)
    if elim:
        k = 0
        for i in range(len(j)):
            pile.pop(j[i]-k)
            k += 1
    print("%d.  " %c, pile)
