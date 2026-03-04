t = (12, 45, 23, 67, 34)

largest = t[0]

for n in t:
    if n > largest:
        largest = n

print("Largest:", largest)

t = (1,2,3,1,1,4)

count = 0

for n in t:
    if n == 3:
        count += 1

print(count)