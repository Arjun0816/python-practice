def greet():
    print("Welcome to python")
greet()

def add(a,b):
    print("Sum =",a+b)

add(15,25)

def square(num):
    return num * num
result = square(7)
print(result)

def check_even(num):
    if num % 2 == 0:
        return ("even")
    else:
        return ("odd")
print(check_even(24))