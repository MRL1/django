# 单继承和多继承

class Person():
    def __init__(self):
        print('WORKING...')


class Bird():
    def __init__(self):
        print("flying....")

    def fly(self):
        print("flying....")


class Fish():
    def __init__(self):
        print("swimming...")

    def swim(self):
        print("swimming....")


class SuperMan(Person, Bird, Fish):
    pass


s = SuperMan()
s.fly()
s.swim()


# 多继承的菱形继承/钻石继承
# 多个子类继承同一个类，这些子类被同一个类继承
class A():
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass
