###---基本操作---###
#符合条件
a = 1
while a < 10:
    print(a)
    a += 1

#含有某项
a = [1,2,3,1,2,1,4,5,3,1]
while 1 in a:
    a.remove('1')

""" 
while <条件>:
    <执行内容>
"""

###---小技巧---###
while True:  # 直接进入执行
    pass