# 类和对象的三种方法
# 实例方法：对象调用的方法
# 静态方法：直接使用类名调用的方法，无参数
# 类方法

class Person():
    # 实例方法
    def play(self):
        print('playing...')

    # 静态方法
    @staticmethod
    def eat():
        print('eatting...')

    # 类方法
    # cls:区分实例方法的self，不是关键字
    @classmethod
    def study(cls):
        print('studying...')

# 调用
p = Person()
p.play()

Person.eat()
Person.study()