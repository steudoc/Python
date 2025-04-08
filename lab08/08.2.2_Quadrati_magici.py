def initM(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            val = int(input("Inserire valore pos [%d][%d]: " %(i,j)))
            matrix[i].append(val)
    return matrix

def printM(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("%2.d" %(matrix[i][j]), end= " ")
        print()
    return

def control(matrix):
    for i in range(len(matrix)):

def main():
    n = int(input("Inserire lato quadrato: "))
    quadrato = initM(n)
    print()
    printM(quadrato)
    return

main()
