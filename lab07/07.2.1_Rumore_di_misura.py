import random

def generate(n):
    lista = []
    for i in range(n):
        lista.append(round(random.uniform(0, 2.50), 2))
    return lista

def approx(lista):
    for i in range(len(lista)):
        if i==0:
            lista[i]=round((lista[i]+lista[i+1])/2, 2)
        elif i==len(lista)-1:
            lista[i]=round((lista[i]+lista[i-1])/2, 2)
        else:
            lista[i]=round((lista[i-1]+lista[i]+lista[i+1])/3, 2)
    return lista

def main():
    n=10
    lista = generate(n)
    print(lista)
    lista = approx(lista)
    print("\nLista corretta = ", lista)
    return

main()
