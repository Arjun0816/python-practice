text = input("Enter a name: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
    
text = ("education")
count = 0
for ch in text:
    if ch in "aeiouAEIOU":
        count = count+1
print("vowels: ",count)

text = "hello world python"
result = text.replace(" ","")
print (result)

text = "papaya"
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
print(freq)

text = input("Enter a word: ").lower()

left = 0
right = len(text) - 1
is_palindrome = True

while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")