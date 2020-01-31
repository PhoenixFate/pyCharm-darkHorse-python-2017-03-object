class Cat:
    def __init__(self):
        print("创建对象的时候会调用初始化方法__init__")
        self.name = "tom"

    def eat(self):
        print("eat")

    def drink(self):
        print("drink")


tom = Cat()
tom.eat()
tom.drink()
print(tom.name)
