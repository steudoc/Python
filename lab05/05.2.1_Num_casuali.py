def main():
    a=32310901
    b=1729
    m=224
    new=int(input("Inserire valore iniziale: "))
    for i in range(100):
        old=new
        new=random(old, a, b, m)
        print(i+1, ").\t", new)
    return

def random(old, a, b, m):
    new = (a*old+b)%m
    return new

main()
