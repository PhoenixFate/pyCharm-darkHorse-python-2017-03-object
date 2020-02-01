class Animal4:

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


class Dog4(Animal4):

    def bark(self):
        print("汪汪汪")


# 继承的特效：传递性
class XiaoTianQuan4(Dog4):
    def fly(self):
        print("fly")

    def bark(self):
        super().bark()
        # python2.x中的方法 不推荐使用
        Dog4.bark(self)

        print("啸天犬 专有咆哮")


xiao_tian_quan = XiaoTianQuan4()
xiao_tian_quan.fly()
xiao_tian_quan.bark()
