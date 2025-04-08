elenco = input("Nomi file: ")
lista = elenco.split(",")
word = input("Parola da cercare: ")

fp = []

for name in lista:
    fp.append(open(name, "r", encoding='utf-8'))

for i, file in enumerate(fp):
    lines = file.readlines()
    for row in lines:
        if word in row:
            print(lista[i], ": ", row)

