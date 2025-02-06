import random

def generate(n):
    lista=[]
    for i in range(n):
        lista.append(random.randrange(0,99+1))
    return lista

#si potrebbe anche fare ordinando la lista ed escludendo il primo valore

def sum_without_smallest(v):
    v.sort()
    tot=0
    #for i in range(1, len(v)):
        #tot=tot+v[i]
    tot=sum(v)
    return tot

def main():
    n=10
    v = generate(n)
    print(v)
    tot = sum_without_smallest(v)
    print("Somma senza minimo: ", tot)
    return

main()
