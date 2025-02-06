import random

def generate(n):
    lista=[]
    for i in range(n):
        lista.append(random.randrange(0,99+1))
    return lista

def main():
    n=20
    lista = generate(n)
    print("Lista = ", lista)
    lista.sort()
    print("\nLista ordinata = ", lista)
    return

main()
