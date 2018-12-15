# 假设我有一个学生类和一个班级类，想要实现的功能为：
#     执行班级人数增加的操作、获得班级的总人数；
#     学生类继承自班级类，每实例化一个学生，班级人数都能增加；
#     最后，我想定义一些学生，获得班级中的总人数。
class ClassTest():
    __num = 0

    @classmethod
    def addNum(cls):
        cls.__num = cls.__num + 1

    @classmethod
    def getNum(cls):
        return cls.__num

    # 使用魔法函数__new__，创建实例时就调用+1
    def __new__(self, *args, **kwargs):
        ClassTest.addNum()
        return super(ClassTest, self).__new__(self)

class Student(ClassTest):
    def __init__(self):
        self.name = ''


s1 = Student()
s2 = Student()
s2 = Student()
print(ClassTest.getNum())