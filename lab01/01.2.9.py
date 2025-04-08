#Un codice alfanumerico lungo 16 caratteri che alterni le stringhe “abcd” e “1234”.

letters="abcd"
numbers="1234"
stringa=letters+numbers

while len(stringa)<16:
    stringa=stringa+letters+numbers

print(stringa)
