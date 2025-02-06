
fp = open("risultati.txt", "r", encoding='utf-8')
classifica = {}

for row in fp.readlines():
    row  = row.split(":")
    row[0] = row[0].split("-")
    row[1] = row[1].split("-")
    squadra1 = row[0][0].strip()
    squadra2 = row[0][1].strip()
    punti1 = int(row[1][0].strip())
    punti2 = int(row[1][1].strip())

    #classifica --> squadra : giocate, punti, PF, PS, Q

    if squadra1 not in classifica:
        classifica[squadra1]=[0, 0, 0, 0, 0.000]
    if squadra2 not in classifica:
        classifica[squadra2]=[0, 0, 0, 0, 0.000]

    #aggiorno numero di partite
    classifica[squadra1][0] += 1
    classifica[squadra2][0] += 1

    #aggiorno punteggi
    if punti1>punti2:
        classifica[squadra1][1] += 3
        classifica[squadra2][1] += 1
    elif punti2>punti1:
        classifica[squadra1][1] += 1
        classifica[squadra2][1] += 3
    else:
        classifica[squadra1][1] += 2
        classifica[squadra2][1] += 2

    #aggiorno punti fatti
    classifica[squadra1][2] += punti1
    classifica[squadra2][2] += punti2

    #aggiorno punti subiti
    classifica[squadra1][3] += punti2
    classifica[squadra2][3] += punti1

    #aggiorno i quozienti
    classifica[squadra1][4] = classifica[squadra1][2]/classifica[squadra1][3]
    classifica[squadra2][4] = classifica[squadra2][2]/classifica[squadra2][3]

print("SQUADRA              GIOCATE PUNTI       Q     PF    PS")
print("-------------------------------------------------------")
for team in sorted(classifica.items(), key = lambda item : item[1][1], reverse=True):
    print("%.20s" %(team[0]))
fp.close()


