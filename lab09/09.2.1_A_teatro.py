def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("%2.d" %(matrix[i][j]), end=" ")
        print()
    print()
    return

teatro = [
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
    [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
    [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
    [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]
]

command = input("Inserire coordinate posto (x.x) o prezzo (10-50): ")
while command!="":
    if command=="10" or command=="20" or command=="30" or command=="40" or command=="50":
        command = int(command)
        i = 8
        j = 9
        trovato = False
        while not trovato and i>=0:
            j = 8
            while not trovato and j>=0:
                if teatro[i][j]==command:
                    teatro[i][j] = 0
                    trovato = True
                else:
                    j -= 1
            i -= 1
        if trovato:
            print("Prenotato posto in posizione [%d, %d]" %(i+1,j))
        else:
            print("Posto di prezzo %d non trovato, scegliere un altro posto" %command)
    else:
        row = command[0]
        row = int(row)
        column = command[2:]
        column = int(column)
        if teatro[row][column] != 0:
            print("Posto prenotato, costo %d" %teatro[row][column])
            teatro[row][column] = 0
        else:
            print("Posto già venduto, scegliere un altro posto")

    printMatrix(teatro)
    command = input("Inserire coordinate posto (x.x) o prezzo (10-50): ")


