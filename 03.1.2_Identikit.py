stringa=input("Inserire stringa: ")
lettere = 0
maiusc = 0
minusc = 0
cifre = 0
long = len(stringa)

for k in range(long):
    num=ord(stringa[k])
    if (num>64 and num<91):
        maiusc += 1
        lettere += 1
    elif (num>96 and num<123):
        minusc += 1
        lettere += 1
    elif (num>47 and num<58):
        cifre += 1

if lettere==long:
    print("I.\tcontiene soltanto lettere")
    if maiusc==long:
        print("II.\tcontiene soltanto lettere maiuscole")
    elif minusc==long:
        print("III.\tcontiene soltanto lettere minuscole")
elif cifre==long:
    print("IV.\tcontiene soltanto cifre numeriche decimali")
elif cifre>0 and lettere>0:
    print("V.\tcontiene soltanto lettere e cifre")

if ord(stringa[0])>64 and ord(stringa[0])<91:
    print("VI.\tinizia con una lettera maiuscola")
if ord(stringa[long-1])==46:
    print("VII.\ttermina con un punto")
