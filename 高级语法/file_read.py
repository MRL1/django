import time
# 打开文件
with open(r'test01.txt', 'r', encoding='utf8') as f:
    # 读取文件的第一行
    strLine = f.readline()
    # 此结构能够按行读出文件的所有内容
    while strLine:
        print(strLine)
        strLine = f.readline()
print('*'*30)

with open(r'test01.txt', 'r', encoding='utf8') as f:
    # 将f作为list参数，读取文件的全部内容
    l = list(f)
    for i in l:
        print(i)
print('*'*30)

with open(r'test01.txt', 'r', encoding='utf8') as f:
    # read是按照字符读取内容，read里面可以设置读取的字符数
    # 如果不设置参数，则表示全部读出
    strChar = f.read(2)
    while strChar:
        print(strChar)
        #time.sleep(1)
        strChar = f.read(2)
print('*'*30)

with open(r'test01.txt', 'r', encoding='utf8') as f:
    f.seek(6, 0)
    strr = f.read()
    print(strr)

# tell()函数:用来显示文件读写指针的当前位置
with open(r'test01.txt', 'r', encoding='utf8') as f:
    strChar = f.read(3)
    pos = f.tell()
    while strChar:
        print(strChar)
        print(pos)
        strChar = f.read(3)
        pos = f.tell()

