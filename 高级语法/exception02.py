# 自定义异常 raise
class JRightError(Exception):
    pass

try:
    num1 = int(input("请输入num1："))
    num2 = int(input("请输入num2："))
    sum = num1 + num2
    print(sum)
    raise JRightError
except NameError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("程序不出错就执行我")
finally:
    print("反正我都要执行")