
def print_num(num):
    for item in num:
        if item==num[len(num)-1]:
            print(item)
        else:
            print(item, end=":")
    return

def alpha_omega(num):
    support = list(num)
    maxi = num[0]
    mini = num[0]
    for i in range(1, len(num)):
        if num[i]>maxi:
            maxi = num[i]
        elif num[i]<mini:
            mini = num[i]
    support.remove(maxi)
    support.remove(mini)
    print_num(support)
    return

def pari(num):
    support = list(num)
    for item in num:
        if int(item)%2!=0:
            support.remove(item)
    print_num(support)
    return

def doppia_cifra(num):
    support = list(num)
    for item in num:
        if len(str(item))!=2:
            support.remove(item)
    print_num(support)
    return

def main():
    val = input("Inserire elenco separato da ':' = ")
    num = val.split(":")
    for i in range(len(num)):
        num[i] = int(num[i])
    alpha_omega(num)
    pari(num)
    doppia_cifra(num)
    return

main()
