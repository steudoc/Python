def count_word(string):
    k=0
    for i in range(len(string)):
        if string[i]==" ":
            k += 1
    k += 1
    return k

def main():
    string=input("Inserire stringa: ")
    words=count_word(string)
    print("Parole: ", words)

main()
