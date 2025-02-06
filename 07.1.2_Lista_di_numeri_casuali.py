import random

def rand():
    lista = []
    for i in range(10):
        lista.append(random.randrange(1, 100+1))
    return lista

def indice(lista):
    indexP=[]
    for i in range(10):
        if i%2==0:
            indexP.append(lista[i])
    return indexP

def valore(lista):
    val=[]
    for item in lista:
        if item%2==0:
            val.append(item)
    return val

def inverso(lista):
    inverted=[]
    inverted=list(lista[::-1])
    return inverted

def alpha_omega(lista):
    alpha=[]
    alpha.append(lista[0])
    alpha.append(lista[len(lista)-1])
    return alpha

def stampaLista(list):
    for item in list:
        print(item, end=" ")
    print()
    return

def main():
    lista=rand()
    index=indice(lista)
    val=valore(lista)
    alpha=alpha_omega(lista)
    print("Lista:", end=" ")
    stampaLista(lista)
    print("Valori indice pari: ", end="")
    stampaLista(index)
    print("Valori pari: ", end="")
    stampaLista(val)
    print("Primo e ultimo valore: ", end="")
    stampaLista(alpha)
    return

main()
