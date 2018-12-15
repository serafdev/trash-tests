class Animal:
    def one(self):
        print("ok")

class Dog(Animal):
    def __init__(self):
        print("no")

x = Dog()

x.one()
