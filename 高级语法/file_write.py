# 文件的写操作
with open(r'test01.txt', 'a', encoding='utf8') as f:
    string = 'fdaf你真的很烦'
    f.write(string)


l = ['ni', 'hao','wo ye buzhidao w zai shuosha ']
with open(r'test01.txt', 'a', encoding='utf8') as f:
    f.writelines(l)


# 持久化 pickle
import pickle
a = [23, 'ljy', [173, 58]]
with open(r'test01.txt', 'wb') as f:
    pickle.dump(a,f)

# 反持久化
with open(r'test01.txt', 'rb') as f:
    ff = pickle.load(f)
    print(ff)


# 持久化——sheleve:类似于字典
import shelve
shv = shelve.open(r'student.db')
# 写入
shv['name'] = 'ljy'
shv['age'] = 23

shv.close()

# 读取
shv = shelve.open(r'student.db', writeback=True)
print(shv['name'])
print(shv['age'])
shv['name'] = 'jjjj'
print(shv['name'])
shv.close()

print(help(shelve.open))