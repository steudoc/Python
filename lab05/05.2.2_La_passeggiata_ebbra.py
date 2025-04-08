import random
a=[0,0]
#partenza: (0,0) orientato verso l'alto
for i in range(100):
    decision=random.randrange(1, 4+1)
    if decision==1:
        a[0]=a[0]+1
    elif decision==2:
        a[1]=a[1]+1
    elif decision==3:
        a[0]=a[0]-1
    elif decision==4:
        a[1]=a[1]-1
    print("%d. " %(i+1), a)
