# 生成随机整数，从1-5取出来
# 然后输入一个数字，来猜，如果大于，则打印bigger
# 小了，则打印less
# 如果相等，则打印equal

import random

try:
    inNum = int(input('请输入：'))
except ValueError as e:
    print('请输入正确的数值：')
else:
    ranNum = random.randint(1, 5)
    print(ranNum)
    if inNum > ranNum:
        print('bigger')
    elif inNum < ranNum:
        print('less')
    else:
        print('equal')
l = [i for i in range(1, 10)]
print(l[::-1])