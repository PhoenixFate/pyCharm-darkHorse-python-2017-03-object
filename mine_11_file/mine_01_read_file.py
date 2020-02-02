# open
# read/write
# close

# 1.卡开文件
# 默认以只读 方式打开文件
file = open("README.md")

# 2.去读文件内容
# read默认会读取所有内容
text = file.read()
print(text)
print(len(text))

text = file.read()
print(text)
print(len(text))

# 3.关闭文件
file.close()
