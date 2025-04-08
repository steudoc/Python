# un robot deve prelevare o depositare in magazzino gli articoli.
# il robot parte dal ripiano più basso e comincia a depositare da sinistra a a destra e dal basso all'alto,
# poi l'ordine si inverte: dalla seconda riga va da destra a sinistra e così via.
# d10 = deposita 10 elementi
# p7 = preleva 7 elementi
# pm = elementi massimi in una posizione

#per prelevare articoli parte dalla colonna più a sinistra e si va dall'alto al basso a prelevare, poi passa alla colonna successiva

'''shelf management'''

def printM(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
    return

def drop(shelf, items, PM):     # drop: il robot riempie prima tutto il ripiano più basso da sinistra a destra e poi passa a quello più alto.
    i = len(shelf)-1
    j = 0
    finito = False
    while not finito:
        voids = PM - shelf[i][j]
        if items<=voids:
            shelf[i][j] += items
            items = 0
            finito = True
        else:
            shelf[i][j] += voids
            items -= voids
            j += 1
            if j == len(shelf[i]):
                i -= 1
                j = 0
                if i<0:
                    finito = True
    return items

def pick(shelf, items):     # pick:  va dall'alto al basso e poi alla colonna successiva
    i = 0
    j = 0
    finito = False
    while not finito:
        if shelf[i][j]>=items:
            shelf[i][j] -= items
            items = 0
            finito = True
        else:
            items -= shelf[i][j]
            shelf[i][j] = 0
            i += 1
            if i==len(shelf):
                j += 1
                i = 0
                if j>=len(shelf[i]):
                    finito = True
    return items

def main():
    PM = 9
    shelf = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    end = False
    printM(shelf)
    while not end:
        command = input("Inserisci comando px, dx: ")
        if command == "":
            end = True
        else:
            op = command[0]
            items = int(command[1:])     #dalla pos 1 fino alla fine. Questo perchè posso avere num di più di una cifra
            if op == "d":
                res = drop(shelf, items,PM)
                printM(shelf)
                print("Rest = ", res)
            elif op == "p":
                res = pick(shelf, items)
                printM(shelf)
                print("Rest = ", res)
            else:
                print("Command error")
    return

main()
