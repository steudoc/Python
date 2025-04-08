fp = open("input.txt", "r", encoding='utf-8')
lines = fp.readlines()
freq = {}

for row in lines:
    start = 0
    for i in range(len(row)):
        if not(row[i].isalpha()):
            word = row[start:i].strip("',.")
            start = i
            if (word not in freq) and word!="":
                freq[word] = 1
            elif word!="":
                freq[word] += 1

top = [0,0,0,0,0]
top_word = ["abc", "abc", "abc", "abc", "abc"]
for word in freq:
    mini = min(top)
    if freq[word]>mini:
        i = top.index(mini)
        top[i] = freq[word]
        if word not in top_word:
            top_word[i]=word

for i in range(5):

top.sort()
for i in range(5):
    print(top_word[i], ":", top[i])

fp.close()
