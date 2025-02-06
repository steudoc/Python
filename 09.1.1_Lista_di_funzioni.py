def f1_change(lista):
    change = lista[0]
    lista[0] = lista[len(lista)-1]
    lista[len(lista)-1] = change
    return lista

def f2_shift(lista):
    change = lista[len(lista)-1]
    shift = lista[0]
    for i in range(1, len(lista)):
        shift2 = lista[i]
        lista[i] = shift
        shift = shift2
    lista[0] = change
    return lista

def f3_pari(lista):
    for item in lista:
        if item%2==0:
            item=0
    return lista

def f4_boundary(lista):
    for i in range(1, len(lista)-1):
        lista[i] = max(lista[i-1], lista[i+1])
    return lista

def f5_delete(lista):
    if len(lista)%2==0:
        k = int(len(lista)/2)
        lista.pop(lista[k])
        lista.pop(lista[k+1])
    else:
        k = int(len(lista)/2) + 1
        lista.pop(lista[k])
    return lista

def f6_pari_dispari(lista):
    pari = []
    dispari = []
    for item in lista:
        if item%2==0:
            pari.append(item)
        else:
            dispari.append(item)
    for i in range(len(lista)):
        if len(pari)!=0:
            lista[i] = pari[0]
            pari.pop(0)
        else:
            lista[i] = dispari[0]
            dispari.pop(0)
    return lista

def f7_secondo_max(lista):
    maxi = [0, 0]
    for item in lista:
        if item > maxi[0]:
            maxi[1] = maxi[0]
            maxi[0] = item
    return maxi[1]

def f8_ord_crescente(lista):
    flag = True
    i = 1
    while flag and i<len(lista):
        if lista[i]<=lista[i-1]:
            flag = False
        i += 1
    return flag

def f9_near_duble(lista):
    flag = False
    i = 1
    while not flag and i<len(lista):
        if lista[i]==lista[i-1]:
            flag = True
        i += 1
    return flag

def f10_duble(lista):
    flag = False
    i = 0
    while not flag and i<len(lista):
        j = i+1
        while not flag and i<len(lista):
            if lista[i]==lista[j]:
                flag = True
    return flag

def main():
    lista = [0,1,2,3,4,5,6,7,8,9]
    f1_change(lista)
    f2_shift(lista)
    f3_pari(lista)
    f4_boundary(lista)
    f5_delete(lista)
    f6_pari_dispari(lista)
    f7_secondo_max(lista)
    f8_ord_crescente(lista)
    f9_near_duble(lista)
    f10_duble(lista)
    return

main()
