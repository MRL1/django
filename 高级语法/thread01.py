# 多线程
import  time
import _thread as thread

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
    thread.start_new_thread(loop1, ())

    thread.start_new_thread(loop2, ())
    #time.sleep(2)
    print('结束3：', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)