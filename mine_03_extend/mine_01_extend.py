class Animal:

    def __init__(self):
        pass

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):

    def bark(self):
        print("汪汪汪")


animal = Animal()
animal.eat()
animal.drink()
animal.run()
animal.sleep()

dog = Dog()
dog.eat()
dog.drink()
dog.sleep()
dog.bark()
