import math as cm

def sphere_volume(r):
    volume=(4/3)*cm.pi*r
    return volume

def sphere_surface(r):
    surface=4*cm.pi*r*r
    return surface

def cylinder_volume(r, h):
    volume=(cm.pi*r*r)*h
    return volume

def cylinder_surface(r, h):
    surface=(cm.pi*r*2)*h
    return surface

def cone_volume(r, h):
    volume=1/3*((cm.pi*r*r)*h)
    return volume

def cone_surface(r, h):
    a=cm.sqrt(r*r+h*h)
    surface=cm.pi*r*(r+a)
    return surface

def main():
    r=int(input("Inserire raggio: "))
    h=int(input("Inserire altezza: "))
    Vsphere=sphere_volume(r)
    Ssphere=sphere_surface(r)
    Vcylinder=cylinder_volume(r, h)
    Scylinder=cylinder_surface(r, h)
    Vcone=cone_volume(r, h)
    Scone=cone_surface(r, h)
    print("Volume sfera= %f.\tSuperficie sfera= %f" %(Vsphere, Ssphere))
    print("Volume cilindro= %f.\tSuperficie cilindro= %f" %(Vcylinder, Scylinder))
    print("Volume cono= %f.\tSuperficie cono= %f" %(Vcone, Scone))

main()
