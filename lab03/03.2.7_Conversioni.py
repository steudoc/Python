udm=input("Inserire udm di partenza (ml,l,g,kg,mm,cm,m,km): ")
conv=input("Inserire udm finale (fl,gal,lb, oz, in,ft,mi): ")

if ((udm=="ml" or udm=="l") and (conv=="fl" or conv=="gal")) or ((udm=="g" or udm=="kg") and (conv=="lb" or conv=="oz")) or ((udm=="cm" or udm=="m" or udm=="km") and (conv=="in" or conv=="ft" or conv=="mi")):
    val=int(input("Inserire valore da convertire: "))
    if udm=="ml":
        if conv=="fl":
            val = val*0.033814
        elif conv=="gal":
            val=val*0.000264
    elif udm=="l":
        if conv=="fl":
            val=val*33.81402
        elif conv=="gal":
            val=val*0.264172
    elif udm=="g":
        if conv=="oz":
            val=val*0.035274
        elif conv=="lb":
            val=val*0.002205
    elif udm=="kg":
        if conv=="oz":
            val=val*35.27396
        elif conv=="lb":
            val=val*2.204623
    elif udm=="mm":
        if conv=="in":
            val=val*0.03937
        elif conv=="ft":
            val=val*0.003281
        elif conv=="mi":
            val=val*0.000000621371192
    elif udm=="cm":
        if conv=="in":
            val=val*0.393701
        elif conv=="ft":
            val=val*0.032808
        elif conv=="mi":
            val=val*0.000006
    elif udm=="m":
        if conv=="in":
            val=val*39.37008
        elif conv=="ft":
            val=val*3.28084
        elif conv=="mi":
            val=val*0.000621
    elif udm=="km":
        if conv=="in":
            val=val*39370.08
        elif conv=="ft":
            val=val*3280.84
        elif conv=="mi":
            val=val*0.621371
    print(val)
else:
    print("Impossibile")
