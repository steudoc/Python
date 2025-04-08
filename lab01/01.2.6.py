#Il saldo di un conto bancario dopo il primo, secondo e terzo anno.
# Il conto ha un saldo iniziale di 1000 dollari e vi vengono accreditati interessi annuali al 5%.

saldo=1000

for k in range(3):
    saldo *= 1.05

print(saldo)
