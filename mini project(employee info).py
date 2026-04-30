class Employee:
    company = "TECH CORP"
    def __init__(self,name):
        self.name = name
    def show(self):
        print(self.name,self.company)
e1 = Employee("Arjun")
e1.show()