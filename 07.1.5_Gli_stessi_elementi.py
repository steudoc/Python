def same_set(a,b):
    cerca = True
    same = True
    i = 0
    while cerca:
        j = 0
        trovato=False
        while cerca:
            if a[i]==b[j]:
                trovato = True
                cerca = False
            elif j==len(b)-1 and trovato==False:
                cerca = False
                same = False
            else:
                trovato = False
                j += 1
        i += 1
    return same

def readL(n):
    lista = []
    val = input("Inserire valore lista %s: " %n)
    while val!="":
        lista.append(int(val))
        val = input("Inserire valore lista %s: " %n)
    return lista

def main():
    a=readL("a")
    print()
    b=readL("b")
    same=same_set(a,b)
    if same:
        print("Le due liste contengono gli stessi valori ")
    else:
        print("Le liste sono differenti")
    return

main()
