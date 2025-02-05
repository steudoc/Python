num=input("Inserire numero: ")
min=num
sum=0
max=0
pari=0
dispari=0

while (num!=""):
    num=int(num)
    sum += num
    print("Somma parziale: %d\n" %(sum))
    if (num>max):
        max=num
    elif (num<int(min)):
        min=num
    if (num%2==0):
        pari += 1
    else:
        dispari += 1
    num=input("Inserire numero: ")

print("\nValore minimo acquisito: ", min)
print("Valore massimo acquisito: ", max)
print("Numero valori pari acquisiti: ", pari)
print("Numero valori dipari acquisiti: ", dispari)
