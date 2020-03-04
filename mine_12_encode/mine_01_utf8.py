# *-* coding:utf8 *-8
# 在第一行 增加如上的话，python2.x解释器
# 或者：
# coding=utf8

# 在字符串前面添加u ,告诉解释器这是一个utf8编码的字符串
hello_str = u"hello 中国"
print(hello_str)
# 在python下面 依然是按照单个字节解析的
for c in hello_str:
    print(c)

str1 = b'\u4f60\u597d'

str2 = "中文"
print("%s" % str2.encode())

# string 通过encode方法转为bytes
# bytes 通过decode转为string


str3 = b'\xe4\xb8\xad\xe6\x96\x87'
print("%s " % str3.decode("utf-8"))
print("%s" % str1.decode())
print("%s" % str1.decode('unicode_escape'))
