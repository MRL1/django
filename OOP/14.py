# 抽象类和抽象方法
# 抽象类里可以包含抽象方法和具体方法
# 抽象类中可以有属相和方法
# 抽象类不允许实例化
# 必须继承才能使用，且继承的子类必须实现所有继承来的方法
# 定义
import abc
class Person(metaclass = abc.ABC):
    # 定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义一个抽象类方法
    # @abc.abstractclassmethod
    # def drink(cls):
    #    pass
    #
    # # 定义一个抽象静态方法
    # @abc.abstractstaticmethod
    # def play():
    #     pass

class Student(Person):
    def smoking(self):
        print('老子是学生，我就是要抽烟')
    # def drink(cls):
    #     print('老子是学生，我就是要喝酒')
    # def play():
    #     print('老子是学生，我就是要玩')
s = Student()
s.smoking()