stringa=input("Inserire stringa: ")
maiusc=""
pari=""
vowels=stringa
num=0
pos=""

for i in range(len(stringa)):
    j=ord(stringa[i])
    if (j>64 and j<91):
        maiusc=maiusc+stringa[i]
    if (j%2==0):
        pari=pari+stringa[i]
    if (j==65 or j==97 or j==69 or j==101 or j==73 or j==105 or j==79 or j==111 or j==87 or j==119):
        vowels=vowels[0:i]+"_"+stringa[i+1:len(stringa)+1]
        pos=pos+" "+str(i)
    if (j>47 and j<58):
        num += 1

print("I.\t\tLettere maiuscole: ", maiusc)
print("II.\t\tLettere in posizioni pari nella stringa: ", pari)
print("III.\tUnderscore: ", vowels)
print("IV.\t\tCifre numeriche: ", num)
print("V.\t\tPosizioni vocali: ", pos)
