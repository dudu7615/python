from tkinter import *
import time


top=Tk()
top.wm_title("测试")
top.geometry('500x300')

var = StringVar()  #保存为一个string类型的变量
var.set("0")        #设置初始值
Label(top, text= "测试" , font = ("黑体",14),fg = "red" , width = 12,height = 2).place(x = 20,y = 40,anchor = 'nw') 

while(True):

    time.sleep(1)
    top.update()  #不断更新
    top.after(10) 
    var.set(chr(ord(var.get())+ 1))#为了展示处字符串变化的效果，煞费苦心，#变化的值，此处修改为你的变量
    #我的只能停车收费系统用了车牌识别的API，可将不同车牌这一字符串展示界面
    Label(top, text= var.get() , font = ("黑体",14),fg = "red" , width = 12,height = 2).place(x = 120,y = 40,anchor = 'nw') 
    
top.mainloop() 