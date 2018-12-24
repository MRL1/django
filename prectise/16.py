# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
num = int(input('请输入'))
l = [1,2,3,4,6]
l.append(num)
l.sort()
print(l)