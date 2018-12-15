# 类的成员描述符（属性）
# 为了在类中对类的成员属性进行相关操作而创建的一种方式
# get：获取属性
# set：修改或者添加属性
# delete：删除属性

# property案例
class Person():
    '''
    将name全部转成大写
    将age全部取整
    '''

    def fget(self):
        return self._name

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        pass


    def fgetA(self):
        return self._age

    def fsetA(self, age):
        self._age = int(age)

    def fdelA(self):
        pass
    name = property(fget, fset, fdel)
    age = property(fgetA, fsetA, fdelA)
p = Person()
p.name = 'ljy'
p.age = 22.3
print(p.name)
print(p.age)
