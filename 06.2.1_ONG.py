def ONG(reddito, figli):
    if reddito<20000:
        sussidio=2000
    elif reddito<30000 and figli>=2:
        sussidio=1500
    elif reddito<40000 and figli>=3:
        sussidio=1000
    else:
        sussidio=0
    sussidio=sussidio*figli
    return sussidio

def main():
    r=0
    reddito = []
    figli = []
    r=int(input("Inserire reddito: "))
    while r!=-1:
        reddito.append(r)
        f=int(input("Inserire numero figli: "))
        figli.append(f)
        r=int(input("Inserire reddito: "))
    for i in range(len(reddito)):
        sussidio=ONG(reddito[i],figli[i])
        print("Sussidio famiglia %d: %d" %(i+1, sussidio))

main()
