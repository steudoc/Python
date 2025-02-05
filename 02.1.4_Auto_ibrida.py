km=int(input("Stima chilometri in un anno: "))
costo1=int(input("Costo auto ibrida: "))
carburante1=float(input("Costo carburante auto ibrida: "))
Efficienza1=float(input("Efficienza in km/l auto ibrida: "))
Rivendita1=int(input("Stima valore rivendita auto ibrida (5anni): "))

costo2=int(input("\nCosto auto benzina: "))
carburante2=float(input("Costo carburante auto benzina: "))
Efficienza2=float(input("Efficienza in km/l auto benzina: "))
Rivendita2=int(input("Stima valore rivendita auto benzina (5anni): "))

totale1=costo1+((km/Efficienza1)*carburante1)-Rivendita1
totale2=costo2+((km/Efficienza2)*carburante2)-Rivendita2

print("\nCosto totale auto ibrida per 5 anni: ", totale1)
print("Costo totale auto benzina per 5 anni: ", totale2)
