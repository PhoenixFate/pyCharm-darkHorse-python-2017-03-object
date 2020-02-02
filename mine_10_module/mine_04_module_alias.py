# 模块别名应该满足 大驼峰命名法
import mine_01_module1 as DogModule
import mine_02_module2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)
cat = CatModule.Cat()
print(cat)
