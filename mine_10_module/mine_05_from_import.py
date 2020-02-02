from mine_01_module1 import Dog
from mine_01_module1 import title
# 如果从两个不同的模块，导入同名函数，后导入的会覆盖前导入的
# 使用as，可以解决这种问题
from mine_01_module1 import say_hello as module1_say_hello
from mine_02_module2 import say_hello

print(title)
module1_say_hello()
say_hello()
dog = Dog()

print(dog)
