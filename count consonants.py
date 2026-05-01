name= input("Enter a string: ")
count = 0
for i in name:
    if i.isalpha() and i not in "aeiouAEIOU":
       count += 1
print("consonants:",count)