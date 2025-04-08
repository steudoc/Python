from math import pi

def diameter(wire_gauge):
    x=(36-wire_gauge)/39
    d=0.127*(92**x)
    return d

def copper_wire_resistance(length, wire_gauge):
    d=diameter(wire_gauge)
    Rc=(4*1.678*(10**-8)*length)/(pi*d*d)
    return Rc

def aluminium_wire_resistance(length, wire_gauge):
    d=diameter(wire_gauge)
    Ra=(4*2.82*(10**-8)*length)/(pi*d*d)
    return Ra

def main():
    wire_gauge=float(input("Inserire calibro: "))
    length=float(input("Inserire lunghezza filo: "))
    Rc=copper_wire_resistance(length, wire_gauge)
    Ra=aluminium_wire_resistance(length, wire_gauge)
    print("Rame: ", Rc)
    print("Alluminio: ", Ra)

main()
