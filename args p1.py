def multiply(*data):
    result = 1
    for i in data:
        result *= i
    print(result)
multiply(2,3,4)