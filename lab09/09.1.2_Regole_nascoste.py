
def f1(l, n):
    for i in range(n):
        l.append(i+1)

    print(l)
    return

def f2(l,n):
    k = 0
    for i in range(n):
        l[i] = k
        k += 2

    print(l)
    return

def f3(l,n):
    for i in range(n):
        l[i]=(i+1)**2

    print(l)
    return

def f4(l,n):
    for i in range(n):
        l[i]=0

    print(l)
    return

def f5(l,n):

    return

def f6(l,n):
    for i in range(n):
        if i%2==0:
            l[i]=0
        else:
            l[i]=1

    print(l)
    return

def f7(l,n):
    k = 0
    for i in range(n):
        l[i]=k
        k += 1
        if k>4:
            k = 0

    print(l)
    return

def main():
    l = []
    n = 10
    f1(l,n)
    f2(l,n)
    f3(l,n)
    f4(l,n)
    f5(l,n)
    f6(l,n)
    f7(l,n)
    return

main()
