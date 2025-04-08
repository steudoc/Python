voto=input("Inserire voto in lettere: ")+" "

if voto[0]=="A":
    num=4.0
    if voto[1]=="-":
        num -= 0.3
elif voto[0]=="B":
    num=3.0
elif voto[0]=="C":
    num=2.0
elif voto[0]=="D":
    num=1.0
elif voto[0]=="F":
    num=0.0

if voto[1]=="+" and num!=0 and num!=4:
    num += 0.3
elif voto[1]=="-" and num!=0:
    num -= 0.3

print("Voto numerico: ", num)
