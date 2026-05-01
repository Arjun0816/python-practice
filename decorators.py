def decor(func):
    def inner():
        print("before")
        func()
        print("after")
    return inner
@decor
def greet():
    print("hello")
greet()