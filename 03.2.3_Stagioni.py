month=int(input("Inserire mese: "))
day=int(input("Inserire giorno: "))

if month>0 and month<4:
    season="Winter"
elif month>3 and month<7:
    season="Spring"
elif month>6 and month<10:
    season="Summer"
elif month>9 and month<13:
    season="Fall"
else:
    season="Il mese inserito non esiste "

if month%3==0 and day>=21:
    if season=="Winter":
        season="Spring"
    elif season=="Spring":
        season="Summer"
    elif season=="Summer":
        season="Fall"
    else:
        season="Winter"

print(season)
