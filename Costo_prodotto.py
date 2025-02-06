
fp = open("exchange.txt", 'r', encoding='utf-8')
conv = fp.readlines()
fp.close()

name = input("Inserire nome file: ")
fp = open(name, 'r', encoding='utf-8')
prod = fp.readlines()
fp.close()


