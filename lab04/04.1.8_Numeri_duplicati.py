num="a"
tot=""
duplicati=""
while (num!=""):
    num=input("Inserire numero: ")
    tot=tot+num

for i in range(1,len(tot)):
    if tot[i]==tot[i-1] and tot[i] not in duplicati:
        duplicati=duplicati+tot[i]+" "

print(duplicati)
