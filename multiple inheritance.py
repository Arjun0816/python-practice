class Father:
    def money(self):
        print("Money")

class Mother:
    def care(self):
        print("Care")

class Child(Father, Mother):
    pass

c = Child()
c.money()
c.care()