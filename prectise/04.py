# 学习成绩>=90分的同学用A表示，60-89分之间的用B表示， 60分以下的用C表示
score = int(input('请输入成绩：'))

if score >= 90:
    print('A')
if score >=60 and score <= 89:
    print('B')
if score < 60:
    print('C')