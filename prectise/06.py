# 求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
num = int(input('基数：'))
times = int(input('次数：'))
l = []
Tn = 0
for i in range(times):
    Tn = Tn + num
    num = num * 10
    l.append(Tn)

print(l)
print(sum(l))