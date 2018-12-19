from functools import reduce
# 匿名函数
stm = lambda x, y: x + y
print(stm(1, 2))

# 高阶函数：把函数作为参数使用
def printC(n):
    return n* 3

def mul(n,f):
    return printC(n) * 100

print(mul(3,3))

# map
# 映射，把集合里的每个元素按照一定规则进行操作，生成一个新的列表
l1 = [i for i in range(0, 10)]

def mulTen(n):
    return n * 10
l3 = []
l2 = map(mulTen, l1)
for i in l2:
    print(i)
    l3.append(i)
print(l3)


# reduce  归并，缩减
l = [1,2,3,4,5]

def add(m, n):
    return m + n
print(reduce(add, l))
