import win32com.client
from tkinter import *
from tkinter import filedialog

speaker = win32com.client.Dispatch("SAPI.SpVoice").Speak


root = Tk()
root.geometry('300x70')
root.title("Reader")

def read():
    speaker(r2.get())

def txt():
    name = filedialog.askopenfilename(filetypes=[("文本文件",".txt")])
    file1 = open(name,'r',encoding='utf8')
    speaker(file1.read())

r1 = Button(root,text="开始朗读",font=("微软雅黑",8),fg="green",command=read)
r1.place(x=240,y=35,height=25, width=50)

r2 = Entry(root,text="",font=("微软雅黑",15))
r2.place(x=10,y=10,height=50, width=220)

r3 = Button(root,text="浏览文件",font=("微软雅黑",8),fg="green",command=txt)
r3.place(x=240,y=10,height=25, width=50)

root.mainloop()
