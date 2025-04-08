year=int(input("Inserire anno (>1582): "))

if year%4==0:
    if year%100!=0:
        print("Anno bisestile")
    else:
        if year%400==0:
            print("Anno bisestile")
        else:
            print("Anno non bisestile")
else:
    print("Anno non bisestile")
