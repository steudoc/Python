
plotter = []
n = 5

for i in range(n):
    plotter.append([])
    for j in range(n):
        plotter[i].append('.')

fp = open("plotter.txt", "r", encoding='utf-8')

for row in fp.readlines():
    row = row.strip().split(" ")
    if row[0]=='P':
        x = n-1-int(row[1])
        y = int(row[2])
        plotter[x][y] = '*'
    elif row[0]=='H':
        x = int(row[1])
        y = n-1-int(row[2])
        l = int(row[3])
        for i in range(l):
            try:
                if plotter[y][x+l] == '|':
                    plotter[y][x+l] = '+'
                else:
                    plotter[y][x+l] = '-'
    else:
        x = int(row[1])
        y = int(row[2])
        l = int(row[3])
        for i in range(l):
            try:
                if plotter[y-l][x] == '-':
                    plotter[y-l][x] = '+'
                else:
                    plotter[y-l][x] = '|'

fp.close()

for i in reversed(range(n)):
    for j in range(n):
        print(plotter[i][j], end=' ')
    print()
