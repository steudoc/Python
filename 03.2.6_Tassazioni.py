reddito=int(input("Inserire valore del reddito: "))
stato=input("Inserire stato civile [C=coniugato][NC=non coniugato]: ")

if stato=="NC":
    if reddito<8000:
        tasse=reddito*0.1
    elif reddito<32000:
        tasse=800+((reddito-8000)*0.15)
    else:
        tasse=4400+((reddito-32000)*0.25)
else:
    if reddito<16000:
        tasse=reddito*0.1
    elif reddito<64000:
        tasse=1600+((reddito-16000)*0.15)
    else:
        tasse=8800+((reddito-64000)*0.25)

print("\nTasse: ", tasse)
