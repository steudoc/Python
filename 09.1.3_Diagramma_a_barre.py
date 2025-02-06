
def valori():
    val = input("Inserire valore: ")
    lista = []
    while val!="":
        lista.append(int(val))
        val = input("Inserire valore: ")
    return lista

def major(lista):
    maxi=0
    for i, item in enumerate(lista):
        if item>maxi:
            maxi = item
            pos = i
    return maxi, pos

def graf(lista, maxi, pos):
    stat = []
    for i in range(len(lista)):
        if i==pos:
            stat.append(40)
        else:
            x = round((40*lista[i])/maxi)
            stat.append(x)
    return stat

def print_graf(stat):
    for i in range(len(stat)):
        print("*"*stat[i])
    return

def main():
    lista = valori()
    maxi, pos = major(lista)
    stat = graf(lista, maxi, pos)
    print_graf(stat)
    return

main()
