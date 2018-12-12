# 构造函数
# class Dog():
#     # __init__就是构造函数
#     # 构造函数的作用就是初始化：每一次实例化时，第一个被自动调用
#     def __init__(self, name):
#         print("你是条狗，英文名字是{}".format(name))
# # 实例化时，括号内的参数需要跟构造函数匹配，否则会报错
# d = Dog('dog')

# 构造函数如果本类中没有定义，则自动查找调用父类构造函数
class Animal():
    pass
class PaxingAnimal(Animal):
    def __init__(self):
        print("哺乳动物")
class Dog(PaxingAnimal):
    def __init__(self):
        print("小奶狗")
    pass
class Cat(PaxingAnimal):
    super.mro()
#dd = Dog()
cc = Cat()