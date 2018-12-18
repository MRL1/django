import random

# 生成0-1的随机浮点数
num = random.random()
num = int(num * 10)
print(num)
print(type(random.random()))

# 生成指定范围的整数 包含0和100
print(random.randint(0, 100))

# 随机返回序列中的某个值
l = ['str:{}'.format(i) for i in range(0,10)]
for items in l:
    print(items)
print(l)
print('*'*20)
print(random.choice(l))

# 打乱列表 不是生成一个新的列表，是将原列表打乱，返回原来的列表
random.shuffle(l)
print(l)