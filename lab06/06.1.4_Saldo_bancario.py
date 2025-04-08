def conto(yr, saldo, tasso):
    for i in range(yr):
        saldo=saldo+(saldo*(tasso/100))
    return saldo

def main():
    anni=int(input("Inserire anni: "))
    saldo=float(input("Inserire saldo iniziale: "))
    tasso=float(input("Inserire tasso interesse annuo: "))
    saldo_finale=conto(anni, saldo, tasso)
    print("\nSaldo finale: ", saldo_finale)

main()
