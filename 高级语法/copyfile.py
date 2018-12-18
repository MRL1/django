import os.path as op
import shutil
import os
# 复制文件
path = 'cdsvdsv'
if op.exists(path):
    shutil.copy('ljy.txt', path)
else:
    path = os.makedirs("C:/Users/LJY/Desktop/kkkkk")
    shutil.copy('ljy.txt', path)

print(op.exists('ljy.txt'))