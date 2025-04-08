def initM(name):
    val = input("Inserire valore lista %s: " %name)
    lista = []
    while val!="":
        lista.append(val)
        val = input("Inserire valore lista %s: " %name)
    print()
    return lista

def merge(a, b):
    new_list =[]
    if len(a)<len(b):
        M=len(b)
        m=len(a)
        flag = False
    else:
        M=len(a)
        m=len(b)
        flag = True
    for i in range(M):
        if i < m:
            new_list.append(a[i])
            new_list.append(b[i])
        elif flag:
            new_list.append(a[i])
        else:
            new_list.append(b[i])
    return new_list

def main():
    a = initM("a")
    b = initM("b")
    new_list = merge(a, b)
    print(new_list)
    return

main()
