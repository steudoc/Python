import random

def lancio(n):
    dadi = []
    for i in range(n):
        dadi.append(random.randrange(1, 6+1))
    return dadi

def serie(dadi):
    longest_length = 0
    longest_pos = 0
    for i in range(1, len(dadi)):
        current_length = 1
        pos = i+1
        while pos<len(dadi) and dadi[pos]==dadi[pos-1]:
            current_length += 1
            pos += 1
        if current_length>longest_length:
            longest_length = current_length
            longest_pos = i
    return longest_length, longest_pos

def correzione(dadi):
    longest_length, longest_pos = serie(dadi)
    dadi.insert(longest_pos, "(")
    dadi.insert(longest_pos+longest_length+1, ")")
    return dadi

def main():
    n=20
    dadi = lancio(n)
    print(dadi)
    dadi = correzione(dadi)
    print(dadi)
    return

main()
