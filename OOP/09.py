# 类的常见魔法函数:不需要人为调动，在特定的时刻触发
# __call__:对象当函数时触发
class Person():
    name = 'ljy'
    age = 0
    def __call__(self, *args, **kwargs):
        print('llllllll')
    def __str__(self):
        return '我是对象字符串'
    def __repr__(self):
        return '222222222'

    # 访问一个不存在的属性时触发
    def __getattr__(self, item):
        print(item)  # 打印不存在的属性名称
        return "找不到"

p = Person()
# p()

# __str__：对象当字符串时触发
p

# __repr__:返回字符串
print(p)

print(dir(p))

print(p.hobby)

