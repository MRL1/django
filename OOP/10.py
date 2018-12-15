# __setattr__案例
class Person():
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        print('设置属性{0},值为{1}'.format(key, value))
        # 这里赋值会导致死循环
        # self.key = value
        # 规定调用父类的魔法函数
        super().__setattr__(key, value)


p = Person()
print(p.__dict__)
p.age = 18


# __gt__案例：进行大于判断时触发
class Student():
    def __init__(self, name):
        self._name = name

    # 第二个参数other是第二个对象
    def __gt__(self, other):
        print('哈哈，{0}会比{1}大吗'.format(self, other))
        return self._name > other._name

    def __str__(self, *args):
        return 'xxxx' 'ssss'

stu1 = Student('ljy')
stu2 = Student('JRight')

print(stu1 < stu2)
