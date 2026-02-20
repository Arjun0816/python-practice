List  = [1,2,2,3,3,6,6,5,5,5]
unique = []
for n in List:
    if n not in unique:
        unique.append(n)
print(unique)

numbers = [222,444,666,888,333]
largest = second =float('-inf')
for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n
print("second largest:",second)

numbers = [1,2,3,4,5]
k = 2
rotated = numbers[k:] + numbers[:k]
print(rotated)

numbers = [1,2,4,5]
n = len(numbers) + 1
expected = n * (n+1)//2
actual  = sum(numbers)
missing = expected - actual 
print ("misssing number:",missing)