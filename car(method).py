class Car:
    def __init__(self,brand):
        self.brand = brand
    def show(self):
        print("Brand:",self.brand)
c1 = Car("toyato")
c1.show()