""" pip install pywin32 """
from win32com.client import Dispatch
from tkinter import *
from tkinter import filedialog

speaker = Dispatch("SAPI.SpVoice").Speak


app = Tk()
app.geometry('280x70')
app.title("Reader")


def read_text():
    speaker(r3.get("1.0","end"))

def read_file():
    name = filedialog.askopenfilename(filetypes=[("文本文件",".txt")])
    file1 = open(name,'r',encoding='utf8')
    r3.insert(1.0,file1.read())
   
r1 = Button(app,text="开始朗读",font=("微软雅黑",8),fg="green",command=read_text)
r2 = Button(app,text="浏览文件",font=("微软雅黑",8),fg="green",command=read_file)
r3 = Text(app,font=("微软雅黑",10))

r1.place(x=220,y=10,height=25, width=50)
r2.place(x=220,y=35,height=25, width=50)
r3.place(x=10,y=10,height=50, width=200)

app.mainloop()

