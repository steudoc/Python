try:
    name = input("Inserire nome file: ")
    fp = open(name, "r", encoding='utf-8')

    lines = fp.readlines()
    servizi = []
    tot = []

    for i in range(len(lines)):
        lines[i] = lines[i].split(";")

    for row in lines:
        if row[1] not in servizi:
            servizi.append(row[1])
            tot.append(float(row[2]))
        else:
            for i in range(len(servizi)):
                if servizi[i]==row[1]:
                    tot[i] += float(row[2])

    for i in range(len(servizi)):
        print(servizi[i],": ",tot[i])

    fp.close()
except OSError:
    print("Error: file not found.")
