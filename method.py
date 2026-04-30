class Student:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print("hello",self.name)
s1 = Student("arjun")
s1.greet()
