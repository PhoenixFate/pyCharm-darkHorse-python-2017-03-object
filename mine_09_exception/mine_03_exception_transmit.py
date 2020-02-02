def demo1():
    return int(input("请输入一个整数"))


def demo2():
    return demo1()


try:
    print(demo2())

except ValueError:
    print("请输入正确的数字")

except Exception as e:
    print("未知异常：%s" % e)
