#Una frase di chiusura di questa prima esercitazione,
#all'interno di una cornice grafica a vostra scelta,
#che includa il calcolo della percentuale di esercizi che avete portato a compimento.

f=input("Inserire numero di esercizi portati a termine prima fase:")
s=input("Inserire numero esercizi portati a termine seconda fase: ")

first=float(f)
second=float(s)

p1=(first*100)/7
p2=(second*100)/15

per1=int(p1)
per2=int(p2)

percent1=str(per1)
percent2=str(per2)

if len(percent1)<2:
    percent1="00"+percent1
elif len(percent1)<3:
    percent1="0"+percent1

if len(percent2)<2:
    percent2="00"+percent2
elif len(percent2)<3:
    percent2="0"+percent2

print("+----------------------------------------------+")
print("|     L'esercitazione 1 è stata completata!    |")
print("|   Percentuale completamento fase 1: ",percent1,"%   |")
print("|   Percentuale completamento fase 2: ",percent2,"%   |")
print("+----------------------------------------------+")
