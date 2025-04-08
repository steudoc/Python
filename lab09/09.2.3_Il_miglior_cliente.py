def init():
    customers = []
    sales = []
    name = input("Insert name customer: ")
    while name != "":
        customers.append(name)
        shop = int(input("Insert sales %s: " %name))
        sales.append(shop)
        name = input("Insert name customer: ")
    return customers, sales

def name_of_best_custumer(sales, customers):
    maxi = 0
    pos = 0
    for i in range(len(sales)):
        if sales[i]>maxi:
            maxi = sales[i]
            pos = i
    return customers[pos]

def main():
    customers, sales = init()
    name = name_of_best_custumer(sales, customers)
    print(name)
    return

main()
