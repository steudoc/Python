def forza(rho,A,Cd,v):
    F=(rho*v*v*A*Cd)/2
    return F

def wattPower(F,v):
    watt=F*v
    return watt

def horsePower(w):
    Hp=w/745.7
    return Hp

def main():
    rho=1.23
    A=2.5
    Cd=0.2
    v=float(input("Inserire velocità dell'auto: "))
    F=forza(rho,A,Cd,v)
    watt=wattPower(F,v)
    cavalli=horsePower(watt)
    print("Potenza= %.2f watt = %.2f cavalli" %(watt, cavalli))

main()
