
from tkinter import *

list_y = []
list_n = []

###设置函数
#否
def n_1():
    while 1 in list_y:
        list_y.remove(1)
    list_n.append(1)
def n_2():
    while 2 in list_y:
        list_y.remove(2)
    list_n.append(2)
def n_3():
    while 3 in list_y:
        list_y.remove(3)
    list_n.append(3)
def n_4():
    while 4 in list_y:
        list_y.remove(4)
    list_n.append(4)
def n_5():
    while 5 in list_y:
        list_y.remove(5)
    list_n.append(5)
def n_6():
    while 6 in list_y:
        list_y.remove(6)
    list_n.append(6)
def n_7():
    while 7 in list_y:
        list_y.remove(7)
    list_n.append(7)        
def n_8():
    while 8 in list_y:
        list_y.remove(8)
    list_n.append(8)
def n_9():
    while 9 in list_y:
        list_y.remove(9)
    list_n.append(9)
def n_0():
    while 0 in list_y:
        list_y.remove(0)
    list_n.append(0)

#是
def y_1(): 
    while 1 in list_n:
        list_y.remove(1)  
    list_y.append(1)
def y_2():
    while 1 in list_n:
        list_y.remove(2)  
    list_y.append(2)
def y_3():
    while 1 in list_n:
        list_y.remove(3)  
    list_y.append(3)
def y_4():
    while 1 in list_n:
        list_y.remove(4)  
    list_y.append(4)
def y_5():
    while 1 in list_n:
        list_y.remove(5)  
    list_y.append(5)
def y_6():
    while 1 in list_n:
        list_y.remove(6)  
    list_y.append(6)
def y_7():
    while 1 in list_n:
        list_y.remove(7)  
    list_y.append(7)        
def y_8():
    while 1 in list_n:
        list_y.remove(8)  
    list_y.append(8)
def y_9():
    while 1 in list_n:
        list_y.remove(9)  
    list_y.append(9)
def y_0():
    while 1 in list_n:
        list_y.remove(0)  
    list_y.append(0)
a = Tk()  #创建窗口

a.geometry("1000x700")  #窗口大小

a.title('智能草稿纸')  #窗口标题


###选择按钮
#是
y1 = Button(a,text="1",font=("微软雅黑",25),fg="green",command=y_1)
y1.place(x=0,y=0,height=30, width=30)

y2 = Button(a,text="2",font=("微软雅黑",25),fg="green",command=y_2)
y2.place(x=30,y=0,height=30, width=30)

y3 = Button(a,text="3",font=("微软雅黑",25),fg="green",command=y_3)
y3.place(x=60,y=0,height=30, width=30)

y4 = Button(a,text="4",font=("微软雅黑",25),fg="green",command=y_4)
y4.place(x=90,y=0,height=30, width=30)

y5 = Button(a,text="5",font=("微软雅黑",25),fg="green",command=y_5)
y5.place(x=120,y=0,height=30, width=30)

y6 = Button(a,text="6",font=("微软雅黑",25),fg="green",command=y_6)
y6.place(x=150,y=0,height=30, width=30)

y7 = Button(a,text="7",font=("微软雅黑",25),fg="green",command=y_7)
y7.place(x=180,y=0,height=30, width=30)

y8 = Button(a,text="8",font=("微软雅黑",25),fg="green",command=y_8)
y8.place(x=210,y=0,height=30, width=30)

y9 = Button(a,text="9",font=("微软雅黑",25),fg="green",command=y_9)
y9.place(x=240,y=0,height=30, width=30)

y0 = Button(a,text="0",font=("微软雅黑",25),fg="green",command=y_0)
y0.place(x=270,y=0,height=30, width=30)


#否
n1 = Button(a,text="1",font=("微软雅黑",25),fg="red",command=n_1)
n1.place(x=0,y=30,height=30, width=30)

n2 = Button(a,text="2",font=("微软雅黑",25),fg="red",command=n_2)
n2.place(x=30,y=30,height=30, width=30)

n3 = Button(a,text="3",font=("微软雅黑",25),fg="red",command=n_3)
n3.place(x=60,y=30,height=30, width=30)

n4 = Button(a,text="4",font=("微软雅黑",25),fg="red",command=n_4)
n4.place(x=90,y=30,height=30, width=30)

n5 = Button(a,text="5",font=("微软雅黑",25),fg="red",command=n_5)
n5.place(x=120,y=30,height=30, width=30)

n6 = Button(a,text="6",font=("微软雅黑",25),fg="red",command=n_6)
n6.place(x=150,y=30,height=30, width=30)

n7 = Button(a,text="7",font=("微软雅黑",25),fg="red",command=n_7)
n7.place(x=180,y=30,height=30, width=30)

n8 = Button(a,text="8",font=("微软雅黑",25),fg="red",command=n_8)
n8.place(x=210,y=30,height=30, width=30)

n9 = Button(a,text="9",font=("微软雅黑",25),fg="red",command=n_9)
n9.place(x=240,y=30,height=30, width=30)

n0 = Button(a,text="0",font=("微软雅黑",25),fg="red",command=n_0)
n0.place(x=270,y=30,height=30, width=30)


label_y=StringVar()
label_n=StringVar()
#结果
label_y = Label(a, text=list_y)
label_y.place(x=300,y=0,height=30,width=200)  

label_n = Label(a,text=list_n)
label_n.place(x=300,y=30,height=30,width=200) 

#输入框 规则同上
#entry=Entry(a,font=("微软雅黑",25),fg="red")
#entry.place(x=111,y=111)

a.mainloop()
