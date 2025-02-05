word=input("Inserire parola: ")
reverse=""

for i in range(len(word)):
    reverse=reverse+word[len(word)-i-1]

print(reverse)
