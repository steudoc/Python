import random

biglie=random.randrange(10, 101)
primaMossa=random.randrange(0, 2)
computerMode=random.randrange(0, 2)

print("Biglie totali: ", biglie)
if computerMode==0:   #computer modalità stupida
    if primaMossa==0:   #gioca prima l'utente
        print("PRIMA MOSSA ALL'UTENTE")
        while(biglie>=0):
            if (biglie==1):
                print("\nE' rimasta solo una biglia. ", end="")
                pescata=1
            else:
                pescata=int(input("Quante biglie vuoi pescare? (min=1, max=%d): " %(int(biglie/2))))
            biglie=biglie-pescata
            if(biglie==0):
                print("Hai pescato l'ultima biglia, hai perso!")
                biglie=-1
            elif (biglie>1):
                pescata=random.randrange(1, int(biglie/2)+1)
                print("Biglie pescate dal computer: ", pescata)
            elif (biglie==1):
                pescata=1
                print("Biglie pescate dal computer: ", pescata)
            biglie=biglie-pescata
            if(biglie==0):
                print("Il computer ha pescato l'ultima biglia, hai vinto!")
                biglie=-1
    else:   #gioca prima il computer
        print("PRIMA MOSSA AL COMPUTER")
        while(biglie>=0):
            if(biglie>1):
                pescata=random.randrange(1, int(biglie/2)+1)
            elif(biglie==1):
                pescata=1
            print("Biglie pescate dal computer: ", pescata)
            biglie=biglie-pescata
            if(biglie==0):
                print("Il computer ha pescato l'ultima biglia, hai vinto!")
                biglie=-1
            elif(biglie>1):
                pescata=int(input("Quante biglie vuoi pescare? (min=1, max=%d): " %(int(biglie/2))))
            elif(biglie==1):
                print("E' rimasta solo una biglia. ", end="")
            biglie=biglie-pescata
            if(biglie==0):
                print("Hai pescato l'ultima biglia, hai perso!")
                biglie=-1
else:
    print("INTELLIGENTE")
    if (primaMossa==0):
        print("PRIMA MOSSA ALL'UTENTE")
        while(biglie>=0):
            if (biglie==1):
                print("\nE' rimasta solo una biglia. ", end="")
                pescata=1
                biglie=biglie-pescata
            elif (biglie>1):
                pescata=int(input("Quante biglie vuoi pescare? (min=1, max=%d): " %(int(biglie/2))))
                biglie=biglie-pescata
            if(biglie==0):
                print("Hai pescato l'ultima biglia, hai perso!")
                biglie=-1
            elif (biglie>1):
                if (biglie>3 and biglie!=7 and biglie!=15 and biglie!=31 and biglie!=63):
                    run=True
                    while(run):
                        pescata=random.randrange(1, int(biglie/2)+1)
                        parziale=biglie-pescata
                        if (parziale==3 or parziale==7 or parziale==15 or parziale==31 or parziale==63):
                            run=False
                else:
                    pescata=random.randrange(1, int(biglie/2)+1)
                print("Biglie pescate dal computer: ", pescata)
            elif (biglie==1):
                pescata=1
                print("Biglie pescate dal computer: ", pescata)
            biglie=biglie-pescata
            if(biglie==0):
                print("Il computer ha pescato l'ultima biglia, hai vinto!")
                biglie=-1
    else:   #gioca prima il computer
        print("PRIMA MOSSA AL COMPUTER")
        while(biglie>=0):
            if (biglie>1):
                if (biglie>3 and biglie!=7 and biglie!=15 and biglie!=31 and biglie!=63):
                    run=True
                    while(run):
                        pescata=random.randrange(1, int(biglie/2)+1)
                        parziale=biglie-pescata
                        if (parziale==3 or parziale==7 or parziale==15 or parziale==31 or parziale==63):
                            run=False
                else:
                    pescata=random.randrange(1, int(biglie/2)+1)
                print("Biglie pescate dal computer: ", pescata)
            elif (biglie==1):
                pescata=1
                print("Biglie pescate dal computer: ", pescata)
            biglie=biglie-pescata
            if(biglie==0):
                print("Il computer ha pescato l'ultima biglia, hai vinto!")
                biglie=-1
            elif (biglie==1):
                print("\nE' rimasta solo una biglia. ", end="")
                pescata=1
                biglie=biglie-pescata
            elif (biglie>1):
                pescata=int(input("Quante biglie vuoi pescare? (min=1, max=%d): " %(int(biglie/2))))
                biglie=biglie-pescata
            if(biglie==0):
                print("Hai pescato l'ultima biglia, hai perso!")
                biglie=-1
