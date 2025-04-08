def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
    print()
    return

def initM(m,n):
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append(0)
    return matrix

def f2(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j]=1
    return matrix

def scacchiera(matrix):
    flag=True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if flag:
                matrix[i][j]=0
            else:
                matrix[i][j]=1
            flag = not flag
        if len(matrix)%2==0:
                flag = not flag
    return matrix

def f4(matrix):
    for j in range(len(matrix[0])):
        matrix[0][j]=0
        matrix[len(matrix)-1][j]=0
    return matrix

def f5(matrix):
    for i in range(len(matrix)):
        matrix[i][0]=1
        matrix[i][len(matrix[i])-1]=1
    return matrix

def somma(matrix):
    tot = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            tot += matrix[i][j]
    return tot

def main():
    m = int(input("Inserire numero righe: "))
    n = int(input("Inserire numero colonne: "))
    tab = initM(m,n)
    print_matrix(tab)
    tab = f2(tab)
    print_matrix(tab)
    tab = scacchiera(tab)
    print_matrix(tab)
    tab = f4(tab)
    print_matrix(tab)
    tab = f5(tab)
    print_matrix(tab)
    totale = somma(tab)
    print("Somma elementi: ", totale)
    return

main()
