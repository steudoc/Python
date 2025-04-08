x=int(input("Inserire numero: "))

I = not(x>0 and x<100)
II = not(x>0 or x<100)
III = not(x>0 or 100<x)
IV = not(x>0 and x<100 or x==-1)

print("Risultati espressione di partenza:\nI\t", I, "\nII\t", II, "\nIII\t", III, "\nIV\t", IV)

I = not(x>0) or not(x<100)
II = not(x>0) and not(x<100)
III = not(x>0) and not(100<x)
IV = not(x>0 and x<100) and not(x==-1)

print("\nRisultati De Morgan:\nI\t", I, "\nII\t", II, "\nIII\t", III, "\nIV\t", IV)
