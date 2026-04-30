vowels = input("Enter a string: ")
count = 0
for i in vowels:
    if i in "aeiou":
        count +=1
print(count)