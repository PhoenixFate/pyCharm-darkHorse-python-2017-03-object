# is 判断两个内存地址是否一样
# == 判断两个值是否相等

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a == b)
print(a is b)
c = None
# print(c == None)
print(c is None)
