def conv(romani):
    arabi = []
    for i in range(len(romani)):
        if romani[i]=='M':
            arabi.append(1000)
        elif romani[i]=='C':
            arabi.append(100)
        elif romani[i]=='L':
            arabi.append(50)
        elif romani[i]=='X':
            arabi.append(10)
        elif romani[i]=='V':
            arabi.append(5)
        else:
            arabi.append(1)
    return arabi

def sum(romani):
    totale=0
    arabi = conv(romani)
    while len(arabi)!=0:
        if len(arabi)==1 or arabi[0]>=arabi[1]:
            totale=totale+arabi[0]
            arabi.pop(0)
        else:
            differenza=arabi[1]-arabi[0]
            totale=totale+differenza
            arabi=arabi[2:]
    return totale

def main():
    romani=input("Inserire numero romano: ")
    s=sum(romani)
    print(s)

main()
