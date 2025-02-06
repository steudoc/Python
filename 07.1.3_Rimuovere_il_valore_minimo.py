def remove_min(v):
    for i in range(len(v)):
        if i==0:
            mini=v[i]
            pos=i
        else:
            if v[i]<mini:
                mini=v[i]
                pos=i
    v.pop(pos)
    return v

def readV():
    v = []
    val = input("Inserire valore: ")
    while val!="":
        v.append(int(val))
        val = input("Inserire valore: ")
    return v

def main():
    v = readV()
    v = remove_min(v)
    print(v)
    return

main()
