fp = open("input.txt", "r", encoding='utf-8')
lines = fp.readlines()
words = 0

for row in lines:
    for i in range(len(row)):
        if row[i]==" " or row[i]=="\n" or row[i]=="'":
            words += 1

print("Numero parole: ", words)

fp.close()
