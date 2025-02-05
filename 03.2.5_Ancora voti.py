num=float(input("Inserire voto numerico: "))

if num>3.7:
    grade='A'
elif num<=3.7 and num>=3.5:
    grade='A-'
elif num<3.5 and num>=3.3:
    grade='B+'
elif num<3.3 and num>2.7:
    grade='B'
elif num<=2.7 and num>=2.5:
    grade='B-'
elif num<2.5 and num>=2.3:
    grade='C+'
elif num<2.3 and num>1.7:
    grade='C'
elif num<=1.7 and num>=1.5:
    grade='C-'
elif num<1.5 and num>=1.3:
    grade='D+'
elif num<1.3 and num>0.7:
    grade='D'
elif num<=0.7 and num>=0.5:
    grade='D-'
elif num<0.5 and num>=0:
    grade='F'
else:
    grade="Il voto inserito è fuori range (0-4)"

print(grade)
