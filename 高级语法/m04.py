# from...import
from m01 import Student,speak
import sys

stu = Student()
stu.say()
speak()
for p in sys.path:
    print(p)
print(type(sys.path))