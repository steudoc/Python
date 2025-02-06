
def valori():
    did = input("Inserire didascalia: ")
    lista = []
    testo = []
    while did!="":
        testo.append(did)
        val = input("Inserire valore: ")
        lista.append(int(val))
        did = input("Inserire didascalia: ")
    return testo, lista

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

def print_graf(testo, stat):
    for i in range(len(stat)):
        print("%10s" %(testo[i]), end="\t")
        print("*"*stat[i])
    return

def main():
    testo, lista = valori()
    maxi, pos = major(lista)
    stat = graf(lista, maxi, pos)
    print_graf(testo, stat)
    return

main()
