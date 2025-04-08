stringa=input("Inserire stringa: ")
l=len(stringa)

for i in range(l):
    for j in range(l):
        if(stringa[i:j+1] != " "):
            print(stringa[i:j+1])
