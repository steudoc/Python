
lista = []
N = int(input("Inserire dimensione matrice: "))
mat = []
for i in range(N):
    mat.append([])
    for j in range(N):
        mat[i].append(0)

for i in range((N**2)):
    lista.append(i+1)

for x in range(N):
    mat[0][x] = lista[0]
    lista.pop(0)

for y in range(1, N):
    mat[y][N-1] = lista[0]
    lista.pop(0)

for x in reversed(range(N-1)):
    mat[N-1][x] = lista[0]
    lista.pop(0)

for y in reversed(range(N-1, 1)):
    mat[y][0] = lista[0]
    lista.pop(0)

#???

print(mat)
