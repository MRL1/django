# 编写程序, A 继承了 B, 俩个类都实现了 handle 方法, 在 A 中的 handle 方法中调用 B 的 handle 方法
class B():
    def handle(self):
        print('B')

class A(B):
    def handle(self):
        super().handle()
        print('A')
a = A()
a.handle()