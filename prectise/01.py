# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
l = list()
for i in range(1, 5):
    str01 = str(i)
    for j in range(1, 5):
        str02 = str(j)
        for k in range(1, 5):
            str03 = str(k)
            if i != j and i != k and j != k:
                string = str01+str02+str03
                l.append(string)
print(len(l))
for items in l:
    print(items, end='  ')