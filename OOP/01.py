#coding:utf-8
'''
    定义一个学生类
    类里面只能有属性和方法
'''


# 类的命名使用大驼峰
class Student():
    # 学生类里有：姓名，年龄，性别三个属性
    name = None
    age = 0
    sex = None

    # 学生有写作业的方法
    def doHomework(self):
        print("我在写作业")
        return

    # 类的实例化
JRight = Student()

#调用类里面的方法
JRight.doHomework()

#调用类里面的属性
print(JRight.age)
print(JRight.name)
print(JRight.sex)

print(JRight.__dict__)
print()
print(Student.__dict__)