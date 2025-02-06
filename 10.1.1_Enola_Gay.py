
fp = open("10.1.1_input.txt", "r", encoding='utf-8')
lines = fp.readlines()

fp_out = open("10.1.1_output.txt", "w", encoding='utf-8')
for i, row in enumerate(lines):
    fp_out.write("/*"+str(i+1)+"*/"+row)

fp.close()
fp_out.close()
