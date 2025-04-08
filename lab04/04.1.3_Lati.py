n=int(input("Inserire lato: "))

for i in range(n):
    print("*  "*n)

print("\n")

for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()

for i in range(-n+1, 0):
    for j in range(n+i):
        print(" ", end="")
    for j in range(2*(-i)-1):
        print("*", end="")
    print()
