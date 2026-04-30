n = int(input("Enter a number: "))
temp = n
total = 0
while n > 0:
    digit = n % 10
    total += digit ** 3 
    n //= 10
if temp == total:
     print("armstrong")
else:
    print("not armstrong")