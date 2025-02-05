def count_vowels(string):
    vowels = []
    for i in range(len(string)):
        letter=string[i]
        if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
            vowels.append(letter)
    return vowels

def main():
    string=input("Inserire stringa: ")
    vowels=count_vowels(string)
    print(vowels)

main()
