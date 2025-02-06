fp_bad = open("bad_words.txt", "r", encoding='utf-8')
lines = fp_bad.readlines()
bad_words = []
for row in lines:
    bad_words.append(row.lower())
fp_bad.close()

fp_text = open("raw_text.txt", "r", encoding='utf-8')
lines = fp_text.readlines()
for i, row in enumerate(lines):
    lines[i] = row.split(" ")
fp_text.close()

fp_out = open("Censored_text.txt", "w", encoding='utf-8')
for row in lines:
    for item in row:
        if item.lower() in bad_words:
            n = len(item.strip())
            fp_out.write("*"*n+" ")
        else:
            fp_out.write(item+" ")
    #fp_out.write("\n")
fp_out.close()

