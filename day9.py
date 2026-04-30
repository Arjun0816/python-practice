text = "python"
print(text)
print(text[0])
print(len(text))

text = "software"
print(text[0:4])
print(text[-1])

name = "arjun kumar"
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("arjun kumar","pandu"))

text = "python"
reverse = ""
for char in text:
    reverse = char + reverse
print(reverse)