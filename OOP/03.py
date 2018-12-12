# 继承
# 语法
# 父类
class Person():
    name = 'NoName'
    age = 0
    __score = 50  # 私有化成员变量，使用两个下划线表示
    _sex = "男"  # 受保护的成员变量，使用一个下划线表示

    def sleep(self):
        print("我在睡觉")
    def work(self):
        print("make money")


# 子类
# 子类继承父类：将父类放在括号里面
class Student(Person):
    # 子类中定义的成员和父类成员相同，则优先使用子类成员
    name = "ljy"
    # 子类里面可以定义独有的成员属性和方法
    hobby = "reading"
    techang = "lol"
    def swimming(self):
        print("我在游泳")
    def play(self):
        print("玩耍")
    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        super().work()
        self.play()
# 子类初始化
s = Student()

# 子类一旦继承父类，就可以使用父类中的非私有化成员变量
print(s.name)
print(s.age)
print(s.sleep())
print(s._sex)
print(s.hobby)
print(s.techang)
print(s.swimming())
print(s.work())
# 子类无法继承父类的私有成员变量
# print(s.__score)
