# 类和对象的成员分析
class Student():
    name = 'JRight'
    age = 23

    # 关于self
    # 有self参数的函数称为非绑定参数，使用对象调用
    def say(self):
        self.name = 'LJY'
        self.age = 12
        # 如果类方法中需要访问当前类的成员，可以通过__clas__.成员名来访问
        print('我叫{}'.format(__class__.name))
        print('我今年{}'.format(self.age))
    # 无self参数的函数称为绑定参数，只能通过类名来访问
    def hello():
        print('hello')


# 查看Student里所有的属性
Student.__dict__
s = Student()
# s.__dict__
# 没有给对象赋值，表示类和对象指向的是同一块地址，也就是说新建对象是空的
s.say()
# 通过类名来访问绑定参数
Student.hello()

# 查看s里所有的属性
print(s.__dict__)
print(s.name)
print(id(Student.name))
print(id(s.name))

print('*' * 30)
# 以下是给对象赋值了的情况
s.name = 'LJY'
print(id(s.name))
print(id(Student.name))
