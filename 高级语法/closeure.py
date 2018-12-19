# 闭包结构：函数里面嵌套函数，里面函数使用外面函数的参数，外面函数的返回值是里面函数
# 返回闭包时，不能使用循环变量
def count():
    def f(j):
        def g():
            return j * j
        return g
    rst = []
    for i in range(1, 4):
        rst.append(f(i))
    return rst
f1, f2, f3= count()
print(f1())
print(f2())
print(f3())
