# 多态
# 多态是一种思想，不是一种语法
# 多态：同一事物的不同状态，比如动物类里面有猪、猫、狗
# 多态性：同一个方法对不同的对象，有着不同的结果

# Minxin设计模式：采用多继承方式对类的功能进行扩展
class Person():
    name = 'ljy'
    age = 23

    def eat(self):
        print("eating...")

    def sleep(self):
        print("sleepping...")

    def play(self):
        print("playing...")


class Teacher(Person):
    def work(self):
        print("working...")


class Student(Person):
    def study(self):
        print("studying...")


class Tudo(Teacher, Student):
    pass


t = Tudo()
print(Tudo.__mro__)
print(t.__dict__)
print(Tudo.__dict__)

print('*' * 30)


class TeacherMixin():
    def work(self):
        print("working...")


class StudentMixin():
    def work(self):
        print("studying...")


class TodoM(Person, TeacherMixin, StudentMixin):
    pass


tt = TodoM()
print(TodoM.__mro__)
print(tt.__dict__)
print(TodoM.__dict__)
