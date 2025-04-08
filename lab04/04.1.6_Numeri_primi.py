val=int(input("Inserire valore: "))

for i in range(2, val):
    primo=True
    for j in range(2, i):
        if (i%j==0):
            primo=False
    if primo:
        print(i)
