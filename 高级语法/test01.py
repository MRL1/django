# a.实现用户输入用户名和密码，当用户名为 seven且密码为123时，显示登陆成功，否则登陆失败！失败时允许重复输入三次

num = 0
while True:
    count = input('请输入账户：')
    pwd = input('请输入密码：')
    if count == 'seven' and pwd == '123':
        print('登录成功')
        break
    else:
        print('登录失败')
        num += 1
        if num == 3:
            print('输入密码超过3次，请稍后再试')
    