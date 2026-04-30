marks = [87,95,76,92]
print(marks)
print(marks[0])
print(len(marks))
marks.append(89)
marks.remove(76)
print(marks)
for m in marks:
    print(m)

marks1 = [88,96,95,77]
total = 0
for m in marks1:
    total = total + m
print("total = ",total)
print("average = ",total/len(marks1))