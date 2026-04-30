import re
text = " my number is 9876543210"
result = re.findall(r'\d+',text)
print(result)