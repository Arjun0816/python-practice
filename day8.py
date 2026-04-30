def check_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
print(check_even(11))


numbers = [87,45,67,90,21]
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
        print("largest :",largest)

numbers =[76,66,56,77,99]
largest = second = float('-inf')
for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif n >  second  and n != largest:
        second = n
print("second largest :",second)

student = {
    "name": "Arjun",
    "marks": [80, 75, 90]
}

total = sum(student["marks"])
print("Average:", total / len(student["marks"]))


