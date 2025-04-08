stringa=input("Inserire stringa: ")
sottostringa=input("Inserire sottostringa: ")
c = 0
pos =" "

for k in range(20):
    if stringa[k]==sottostringa[0]:
        if stringa[k:k+3]==sottostringa:
            trovato=1
            pos= pos+str(k)+" "
            c += 1
        else:
            trovato=0

if trovato:
    print("I.\tLa sequenza lunga contiene la sequenza breve")
    print("II.\tLa sequenza è presente a partire dalla posizione: ", pos[1:3])
    print("III.\tLa sequenza lunga contiene la sequenza corta ", c,"volte")
else:
    print("Sequenza non trovata")
