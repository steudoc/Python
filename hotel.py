
fp = open("presenze.txt", 'r', encoding='utf-8')
presenze = {}

for row in fp.readlines():
    row = row.strip().split(',')
    presenze[row[0]] = row[1:]

fp.close()

fp = open("sospetti.txt", 'r', encoding='utf-8')
sospetti = {}

for row in fp.readlines():
    row = row.strip()
    sospetti[row] = []

fp.close()

for key in presenze.keys():
    if key in sospetti.keys():
        sospetti[key] = presenze[key]
    else:
        sospetti[key] = False

for

print(sospetti)

