class Person():
    def __init__(self, name, age):
        self.name = name.upper()
        self.age = int(age)
p = Person('ljy',22.5)

print(p.name)
print(p.age)

# 类的内置属性
# __dict__:以字典的形式显示类的成员组成
print(Person.__dict__)

# __doc__获取文档信息
print(Person.__doc__)

# __name__：获取类的名称
print(Person.__name__)

# __bases__：以元祖的形式获取类的所有父类
print(Person.__bases__)
