import os  #os模块是主角
path = "c:/windows"  #绝对路径
a = os.listdir(path)  #获取所有文件名(不包括文件夹)
print(a)
for b in a:  #稍做处理
    print(b)