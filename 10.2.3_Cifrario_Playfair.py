
fp = open("Playfair.txt", "r", encoding='utf-8')
key = input("Inserire chiave: ")

mat = []
mat.append([])
i = 0
for char in key:
    if len(mat[i])==5:
        mat.append([])
        i += 1
    flag = True
    for row in mat:
        if char in row:
            flag = False
    if flag:
        mat[i].append(char)

fp_alfabeto = open("alfabeto.txt", "r", encoding='utf-8')
alfabeto = fp_alfabeto.readlines()
for letter in alfabeto:
    if letter.strip() != 'J':
        if len(mat[i])==5:
            mat.append([])
            i += 1
        flag = True
        for row in mat:
            if letter.strip() in row:
                flag = False
        if flag:
            mat[i].append(letter.strip())
fp_alfabeto.close()

text = fp.readlines()
k = 0
for i in range(len(text)):
    text[i] = text[i].strip('\n').upper()
    for char in text[i]:
        if char.isalpha():
            k += 1
fp.close()
if (k%2) != 0:
    text[-1] = text[-1] + 'Z'

for i in range(len(text)):
    for j in range(len(text[i])):




