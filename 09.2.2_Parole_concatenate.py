wA = input("[Giocatore A] inserisci parola: ")
run = True
while run:
    wB = input("[Giocatore B] inserisci parola: ")
    #print(wB[:1+1])
    #print(wA[len(wA)-2:])
    if wB=="*":
        run = False
    elif wB[:1+1]!=wA[(len(wA)-2):]:
        run = False
        print("[Giocatore B] Hai perso!!!")

    if run:
        wA = input("[Giocatore A] inserisci parola: ")
        if wA=="*":
            run = False
        elif wA[:1+1]!=wB[len(wB)-2:]:
            run = False
            print("[Giocatore A] Hai perso!!!")

