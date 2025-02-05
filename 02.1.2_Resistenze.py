r1=input("Immettere resistenza R1: ")
r2=input("Immettere resistenza R2: ")
r3=input("Immettere resistenza R3: ")

parallelo=1/((1/int(r2))+(1/int(r3)))
tot=int(r1)+parallelo

print("Resistenza totale: ", tot)

