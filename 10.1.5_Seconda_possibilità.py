val = input("Inserire valore: ")
sum = 0
while val!=' ':
    try:
        val = float(val)
        sum += val
        val = input("Inserire valore: ")
    except ValueError:
        print("Error: You have only one restant possibility.")
        val = input("Inserire valore: ")
        while val!=' ':
            try:
                val = float(val)
                sum += val
                val = input("Inserire valore: ")
            except ValueError:
                print("Error!!! Program terminated")
                val = ' '

print("\nSum = ", sum)
