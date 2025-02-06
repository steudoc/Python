import random

def insert(r, c):
    tab = []
    for i in range(r):
        tab.append([])
        for j in range(c):
            tab[i].append(random.randrange(1, 9+1))
    return tab

def neighbor_average(tab, i, j):
    if i==0:
        if j==0:
            avg=(tab[i][j+1]+tab[i+1][j+1]+tab[i+1][j])/3
        elif j==len(tab[i]):
            avg=(tab[i][j-1]+tab[i+1][j-1]+tab[i+1][j])/3
        else:
            avg=(tab[i][j-1]+tab[i+1][j]+tab[i+1][j+1]+tab[i][j+1])/5
    elif i==len(tab)-1:
        if j==0:
            avg=(tab[i-1][j]+tab[i-1][j+1]+tab[i][j+1])/3
        elif j==len(tab[i])-1:
            avg=(tab[i][j-1]+tab[i-1][j-1]+tab[i-1][j])/3
        else:
            avg=(tab[i][j-1]+tab[i-1][j-1]+tab[i-1][j]+tab[i-1][j+1]+tab[i][j+1])/5
    else:
        if j==0:
            avg=(tab[i-1][j]+tab[i-1][j+1]+tab[i][j+1]+tab[i+1][j+1]+tab[i+1][j])/5
        elif j==len(tab[i])-1:
            avg=(tab[i-1][j]+tab[i-1][j-1]+tab[i][j-1]+tab[i+1][j-1]+tab[i+1][j])/5
        else:
            somma=0
            for c in range(i-1, i+1+1):
                for k in range(j-1, j+1+1):
                    if c!=i or k!=j:
                        somma += tab[c][k]
            avg=somma/8
    return avg

def main():
    r=3
    c=3
    values = insert(r, c)
    print(values)
    pos = input("Inserire posizione di cui calcolare la media dell'intorno i.j: ")
    row = int(pos[0])
    column = int(pos[2:])
    average = neighbor_average(values, row, column)
    print("Intorno medio: ", average)
    return

main()
