
def parcheggi(n):
    occupied = []
    for i in range(n):
        occupied.append(False)
    return occupied

def new_parking(occupied):
    longest_lenght = 0
    longest_pos = 0
    for i in range(len(occupied)):
        if not occupied[i]:
            current_length = 1
            pos = i+1
            while pos<len(occupied) and not occupied[pos]:
                current_length += 1
                pos += 1
            if current_length>longest_lenght:
                longest_lenght = current_length
                longest_pos = i

    #  pos = (longest_pos + longest_lenght)//2

    occupied[longest_pos + longest_lenght // 2] = True

    return occupied

def stampa(occupied, n):
    for i in range(n):
        if occupied[i]:
            print("X", end="")
        else:
            print("_", end="")
    print()
    return

def main():
    n = int(input("Inserire numero posteggi: "))
    park = parcheggi(n)
    stampa(park, n)
    run = input("Occupare nuovo posteggio? (0=yes) ")
    while run != "" and False in park:
        park = new_parking(park)
        stampa(park, n)
        run = input("Occupare nuovo posteggio? (0=yes) ")
    return

main()
