#A = crescitaPrede
#B = distruzionePrede
#C = mortalitaPredatori
#D = incrementoPredatori
'''
dx/dt=A*x-B*x*y
dy/dt=-C*y+D*x*y
'''
def aumentoPrede(A, x, dt):
    #aumento prede
    dx=A*x*dt
    return dx

def diminuzionePrede(B,x,y,dt):
    #diminuzione prede
    dx=(-B)*x*y*dt
    return dx

def diminuzionePredatori(C,y,dt):
    #diminuzione predatori
    dy=(-C)*y*dt
    return dy

def aumentoPredatori(D, x, y, dt):
    #aumento predatori
    dy=D*x*y*dt
    return dy

def variazionePrede(A,B,x,y,dt):
    dx=aumentoPrede(A,x,dt)-diminuzionePrede(B,x,y,dt)
    return dx

def variazionePredatori(C,D,x,y,dt):
    dy=aumentoPredatori(D,x,y,dt)-diminuzionePredatori(C,y,dt)
    return dy

def main():
    A=float(input("Inserire tasso crescita prede: "))
    B=float(input("Inserire tasso distruzione prede da parte dei predatori: "))
    C=float(input("Inserire tasso mortalità predatori: "))
    D=float(input("Inserire tasso incremento predatori: "))
    x=int(input("Inserire numerosità iniziale prede: "))
    y=int(input("Inserire numerosità iniziale predatori: "))
    dt=int(input("Inserire periodo che si intende analizzare: "))
    print("Variazione prede: ", variazionePrede(A,B,x,y,dt))
    print("Variazione predatori: ", variazionePredatori(C,D,x,y,dt))

main()
