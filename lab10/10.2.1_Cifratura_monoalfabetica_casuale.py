name = "Cifrario_di_Cesare.txt"#input("Inserire nome file da cifrare/decifrare: ")
command = "C" #input("Inserire comando (C/D): ")
key = "FEATHER" #input("Inserire key word: ")
name_out = "Testo_cifrato.txt" #input("Inserire nome file su cui scrivere output: ")

#try:
fp = open(name, "r", encoding='utf-8')
fp_alfa = open("alfabeto.txt", "r", encoding='utf-8')
fp_out = open(name_out, "w", encoding='utf-8')
alfabeto = fp_alfa.readlines()
fp_alfa.close()
cifrario = []
key = key.upper()
for i in range(len(alfabeto)):
    alfabeto[i] = alfabeto[i].strip()

for char in key:
    if char not in cifrario:
        cifrario.append(char)

for char in reversed(alfabeto):
    if char not in cifrario:
        cifrario.append(char)

for char in fp.read():
    if char in alfabeto:
        for item in alfabeto:
            if item==char:
                i = alfabeto.index(item)
        fp_out.write(cifrario[i])
    else:
        fp_out.write(char)

fp.close()
fp_out.close()

#except Exception as ex:
    #print("Error: ", ex)
