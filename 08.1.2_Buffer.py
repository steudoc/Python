def shift(lista):
    last = lista[len(lista)-1]
    for i in range(len(lista)):
        if i == 0:
            prec = lista[i]
            lista[i] = last
        else:
            act = lista[i]
            lista[i] = prec
            prec = act
    return lista

def main():
    stringa = input("Inserire lista valori: ")
    lista = []
    for i in range(len(stringa)):
        lista.append(stringa[i])
    shift(lista)
    print(lista)
    return

main()
