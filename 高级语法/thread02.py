# threading
import time
import threading
def loop1():
    print('开始1:', time.ctime())
    time.sleep(4)
    print('结束1：', time.ctime())

def loop2():
    print('开始2:', time.ctime())
    time.sleep(2)
    print('结束2：', time.ctime())

def main():
    print('开始3:', time.ctime())
    # loop1()
    # loop2()
    # 启动一个线程
    t1 = threading.Thread(target=loop1, args='')
    # 开启线程
    t1.start()
    t2 = threading.Thread(target=loop2, args='')
    t2.start()
    # time.sleep(2)
    # 等待多线程完成
    t1.join()
    t2.join()
    print('结束3：', time.ctime())

if __name__ == '__main__':
    main()