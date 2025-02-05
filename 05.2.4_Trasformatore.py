def potenza(n):
    p=8*(((n*40)/(n*n*20+8))**2)
    return p

n=0.01
maxi=0
while (n<=2):
    power=potenza(n)
    n += 0.01
    if power>maxi:
        maxi=power
        rapporto=n

print("Potenza massima: ", maxi,". Rapporto spire: ",rapporto)
