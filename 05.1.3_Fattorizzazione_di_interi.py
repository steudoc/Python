def fattorizzazione(val):
    while val>1:
        if val%2==0:
            print(2)
            val=val/2
        elif val%3==0:
            print(3)
            val=val/3
        elif val%5==0:
            print(5)
            val=val/5
        elif val%13==0:
            print(13)
            val=val/13

val=int(input("Inserire numero: "))
print("Fattorizzazione: ")
fattorizzazione(val)
