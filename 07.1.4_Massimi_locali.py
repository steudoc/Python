def readM():
    lista_num = []
    val = input("Inserire valore: ")
    while val!="":
        lista_num.append(int(val))
        val = input("Inserire valore: ")
    return lista_num

def massimi(lista_num):
    lista_max = []
    for i in range(len(lista_num)):
        if i==0:
            if lista_num[i]>lista_num[i+1]:
                lista_max.append(lista_num[i])
        elif i==len(lista_num)-1:
            if lista_num[i]>lista_num[i-1]:
                lista_max.append(lista_num[i])
        else:
            if lista_num[i]>lista_num[i-1] and lista_num[i]>lista_num[i+1]:
                lista_max.append(lista_num[i])
    if lista_max==[]:
        lista_max="Non ci sono massimi locali"
    return lista_max

def main():
    lista_num = readM()
    lista_max = massimi(lista_num)
    print("\nLista massimi locali: ", lista_max)

main()
