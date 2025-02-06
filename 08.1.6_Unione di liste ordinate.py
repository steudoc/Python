def initM(name):
    val = input("Inserire valore lista %s: " %name)
    lista = []
    while val!="":
        lista.append(val)
        val = input("Inserire valore lista %s: " %name)
    print()
    return lista

def merge_sorted(a,b):
    i = 0
    j = 0
    new_sorted = []
    run = True
    while run:
        if i==len(a):
            for k in range(j,len(b)):
                new_sorted.append(b[k])
            run = False
        elif j == len(b):
            for k in range(i,len(a)):
                new_sorted.append(a[k])
            run = False
        else:
            if a[i]<=b[j]:
                new_sorted.append(a[i])
                i += 1
            else:
                new_sorted.append(b[j])
                j += 1
    return new_sorted

def main():
    a = initM("a")
    b = initM("b")
    new_sorted = merge_sorted(a,b)
    print(new_sorted)
    return

main()
