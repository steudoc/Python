#«un numero primo è un numero naturale maggiore di 1 che sia divisibile solamente per 1 e per se stesso»
# n è primo se non è divisibile per nessuno degli interi, k, compresi tra 1 e n, estremi esclusi (1<k<n).
val=int(input("Inserire numero intero: "))
primo=True

for i in range (2, val):
    if (val%i==0):
        primo=False

if primo:
    print(val, "è numero primo")
else:
    print(val, "non è numero primo")
