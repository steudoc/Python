n=input("Inserire numero telefonico a 10 cifre: ")

area_code="("+n[0:3]+")"

numero=area_code+" "+n[3:6]+chr(45)+n[6:10]
print(numero)
