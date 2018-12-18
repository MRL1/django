# 异常处理
try:
    num = int(input("请输入："))
    result = 100 / num
    print("结果为：{}".format(result))
except ZeroDivisionError as e:
    print(e)
    exit()
except NameError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("程序不出错就执行我")
finally:
    print("不管程序出不出错都要执行我")