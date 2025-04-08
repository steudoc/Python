spesa=int(input("Spesa totale: "))
b1=0
b2=0.08
b3=0.1
b4=0.12
b5=0.14

if spesa<10:
    buono=spesa*b1
elif spesa<61:
    buono=spesa*b2
elif spesa<151:
    buono=spesa*b3
elif spesa<211:
    buono=spesa*b4
else:
    buono=spesa*b5

print("Valore buono: ", buono)
