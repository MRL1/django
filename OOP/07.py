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
    def fset(self, name, age):
        self._name = name.upper()
        self._age= int(age)
    def fdel(self):
        self._name = 'NoName'
        self._age = 0
    def fget(self):
        pass

    name = property(fget, fset, fdel)
    age = property(fget, fset, fdel)
p = Person()
p.name = 'ljy '
p.age = '22.3'
print(p.name)
print(p.age)
print(int(22.3))