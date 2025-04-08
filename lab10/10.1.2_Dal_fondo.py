
fp = open("10.1.2_input.txt", "r", encoding='utf-8')
lines = fp.readlines()

fp_out = open("10.1.2_output.txt", "w", encoding='utf-8')
for row in reversed(lines):
    fp_out.write(row)

fp.close()
fp_out.close()
