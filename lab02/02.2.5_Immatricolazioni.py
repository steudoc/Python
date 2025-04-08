m1=input("Inserire prima matricola: ")
m2=input("Inserire seconda matricola: ")

if m1[1:7]>m2[1:7]:
    lista=[m2,m1]
elif m1[1:7]<m2[1:7]:
    lista=[m1,m2]
elif m1[1:7]==m2[1:7]:
    if m1[0:1]>m2[0:1]:
        lista=[m2,m1]
    elif m1[0:1]<m2[0:1]:
        lista=[m1,m2]
    else:
        lista="Le due matricole sono uguali"

print("\n",lista)
