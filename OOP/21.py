# 多重继承
class BaseClass(object):
    def __init__(self, value):
        self.value = value
        print('Init BaseClaa')
        print(self.value)
        print('#' * 20)

class TimesTwo(BaseClass):
    def __init__(self, value):
        #BaseClass.__init__(self, value)
        super(TimesTwo, self).__init__(value)
        self.value *= 2
        print('Init TimesTwoClass')
        print(self.value)
        print('#' * 20)

class PlusFive(BaseClass):
    def __init__(self, value):
        #BaseClass.__init__(self, value)
        super(PlusFive, self).__init__(value)
        self.value += 5
        print('Init PlusFiveClass')
        print(self.value)
        print('#' * 20)

class SubClass(TimesTwo, PlusFive,BaseClass,object):
    def __init__(self, value):
        # TimesTwo.__init__(self, value)
        # PlusFive.__init__(self, value)
        super(SubClass, self).__init__(value)

foo = SubClass(1)
print(foo.value)
print(SubClass.__mro__)