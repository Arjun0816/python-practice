class Animal:
    def sound(self):
        print("animal makes sound")
class Dog(Animal):
    def sound(self):
        print("dog barks")
class Cat(Animal):
    def sound(self):
        print("meow")
d1 = Dog()
c1 = Cat()
d1.sound()
c1.sound()