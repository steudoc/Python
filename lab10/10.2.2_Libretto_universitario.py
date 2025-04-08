
student_id = input("Inserire id studente: ")

fp = open("classes.txt", "r", encoding='utf-8')
student = {}
for file in fp.readlines():
    name = file.strip() + ".txt"
    fp_class = open(name, "r", encoding='utf-8')
    for line in fp_class.readlines():
        line = line.strip().split(" ")
        if line[0] == student_id:
            student[name] = line[1]
    fp_class.close()
print(student)
fp.close()
