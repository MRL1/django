# 模块：包含Python代码的文件
class Student():
    def __init__(self, name = "NoName", age =19 ):
        self.name = name
        self.age = age
        print('hi, 我叫{}，今年{}岁'.format(self.name, self.age))
    def say(self):
        print("i am saying。。。")
