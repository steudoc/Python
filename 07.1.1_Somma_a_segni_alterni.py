def readL():
    list = []
    i=0
    val = input("Inserire valore %d: " %(i))
    while val!="":
        list.append(int(val))
        i += 1
        val = input("Inserire valore %d: " %(i))
    return list

def somma(list):
    tot=0
    for i in range(len(list)):
        if i%2==0:
            tot=tot+list[i]
        else:
            tot=tot-list[i]
    return tot

def main():
    list = readL()
    tot = somma(list)
    print("\nSomma segni alterni = ", tot)
    return

main()
