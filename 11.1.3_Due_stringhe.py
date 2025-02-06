string1 = input("Inserire prima stringa: ")
string2 = input("Inserire seconda stringa: ")
set1 = set()
set2 = set()

for char in string1:
    set1.add(char.lower())
for char in string2:
    set2.add(char.lower())

print("Caratteri in entrambe le stringhe: ", set1.intersection(set2))
print("Caratteri della prima stringa che non compaiono nella seconda: ", set1.difference(set2))
print("Caratteri della seconda stringa che non compaiono nella prima: ", set2.difference(set1))

alfabeto = set()
fp = open("alfabeto.txt", "r", encoding='utf-8')
letters = fp.readlines()
for row in letters:
    alfabeto.add(row.strip().lower())

print("Lettere che non compaiono nelle due stringhe: ", alfabeto.difference(set1.union(set2)))


