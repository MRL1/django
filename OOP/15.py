# 如下示例, 请用面向对象的形式优化以下代码
   # def exc1(host,port,db,charset):
   #     conn=connect(host,port,db,charset)
   #     conn.execute(sql)
   #     return xxx
   # def exc2(host,port,db,charset,proc_name)
   #     conn=connect(host,port,db,charset)
   #     conn.call_proc(sql)
   #     return xxx
   # 每次调用都需要重复传入一堆参数
   # exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
   # exc2('127.0.0.1',3306,'db1','utf8','存储过程的名字')
class Exc():
    '''
    这个类里面有一下属性，并且还有一个执行方法
    '''
    host = '127.0.0.1'
    port = 3306
    db = 'db1'
    charset = 'utf8'
    conn = connect(host, port, db, charset)
    def __init__(self, proc_name):
        self.proc = proc_name
    def test(self):
        if self.proc == 'select * from tb1':
            self.conn.execute(sql)
        if self.proc =='存储过程的名字':
            self.conn.call_proc(sql)
            return XXX
e1 = Exc('select * from tb1')
e1.test()

e2 = Exc('存储过程的名字')
e2.test()

