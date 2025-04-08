
fp = open("rawdata_2004.txt", "r", encoding='utf-8')
lines = fp.readlines()
reddito = {}

for row in lines:
    i = 0
    while not(row[i].isalpha()):
        i += 1
    c = i
    while row[i]!="\t":
        i += 1
    key = row[c:i]
    while not(row[i].isnumeric()):
        i += 1
    num = row[i:len(row)-1]
    reddito[key] = num

run = True
while run:
    try:
        nazione = input("Nazione: ")
        while nazione != "quit":
            print("Reddito annuo pro capite: ", reddito[nazione])
            nazione = input("Nazione: ")
        run = False
    except Exception as exc:
        print("ERROR: ", exc)
