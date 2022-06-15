
from tkinter import *


top=Tk()
top.wm_title("测试")
top.geometry('500x300')

var = IntVar()	#保存为一个int类型的变量
var.set(0)	#设置初始值
count = 0	#通过计数来改变var值
Label(top, text= "测试" , font = ("黑体",14),fg = "red" , width = 12,height = 2).place(x = 20,y = 40,anchor = 'nw') 

while(True):

    count += 1
    top.update()  #不断更新
    top.after(10) 
    if count % 50 == 0:
        var.set( var.get() + 1 )#变化的值，此处修改为你的变量
        Label(top, text= str(var.get()) , font = ("黑体",14),fg = "red" , width = 12,height = 2).place(x = 120,y = 40,anchor = 'nw') 
    
top.mainloop()