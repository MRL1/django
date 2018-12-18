import os

# 得到地址
print(os.getcwd())

# 获取一个目录中所有子目录和文件的名称列表
print(os.listdir())

# 递归创建文件夹
#print(help(os.makedirs))
#print(os.makedirs('ljy'))

# 运行系统shell命令
print(os.system(''))

# 获取指定系统的环境变量值
print(os.getenv('Path'))

print(os.name)