# 一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
team = []
for i in range(3):
    age = int(input('请输入年龄：'))
    sex = input('请输入性别：')
    if age>= 10 and age<=12 and sex == 'f':
        team.append(age)
        print('可以加入')
print(len(team))
