# staticmethod与classmethod的区别
class A():
    # 普通函数
    def foo(self, x):
        print('foo{}'.format(self, x))

    # classmethod
    @classmethod
    def class_foo(cls, x):
        print('class_foo{}'.format(cls, x))

    # staticmethod
    @staticmethod
    def ststic_foo(x):
        print('static_foo{}'.format(x))
a = A()
a.foo('普通函数')


a.class_foo('类函数')
A.class_foo('类函数')

A.ststic_foo('静态函数')
a.ststic_foo('静态函数')


