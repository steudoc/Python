
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
        if i==0:
            mini=item
            maxi=item
            pos=i
        elif item>maxi:
            maxi = item
            pos = i
        elif item<mini:
            mini = item
    return maxi, pos, mini

def graf(lista, maxi, pos):
    stat = []
    for i in range(len(lista)):
        if i==pos:
            stat.append(40)
        else:
            x = round((40*lista[i])/maxi)
            stat.append(x)
    return stat

def print_graf(stat, mini):
    mini = mini*(-1)
    for i in range(len(stat)):
        if stat[i]>=0:
            print(" "*mini,"*"*stat[i])
        else:
            space = mini+stat[i]
            print(" "*space, "*"*((-1)*stat[i]))
    return

def main():
    lista = valori()
    maxi, pos, mini = major(lista)
    stat = graf(lista, maxi, pos)
    print_graf(stat, mini)
    return

main()
