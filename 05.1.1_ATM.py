def control(enter):
    PIN="1234"
    if enter==PIN:
        check = True
    else:
        check = False
    return check

c=0
run=True
while run:
    enter = input("Inserire PIN: ")
    check = control(enter)
    if check:
        print("Your PIN is correct")
        run=False
    else:
        print("Your PIN is incorrect")
        c += 1
        if c==3:
            print("Your bank card is blocked")
            run = False
