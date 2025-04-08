
def discount(prices, is_pet):
    if True in is_pet:
        if len(prices)>5:
            somma = 0
            for i in range(len(prices)):
                if is_pet[i]==False:
                    somma += prices[i]
            sconto = somma*0.20
        else:
            sconto = 0
    else:
        sconto = 0
    return sconto

def main():
    prices = []
    is_pet = []
    costo = int(input("Inserire costo prodotto: "))
    while costo!=-1:
        prices.append(costo)
        pet = input("Il prodotto è un animale? (Y/N): ")
        if pet=="Y":
            is_pet.append(True)
        else:
            is_pet.append(False)
        costo = int(input("Inserire costo prodotto: "))
    sconto = discount(prices, is_pet)
    print("Sconto = ", sconto)
    return

main()
