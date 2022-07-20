from tkinter import *

app = Tk()
app.geometry('500x300')
app.title("小说下载")

num = 0

while True:
    if num < 36:
        num += 1
    else:
        num = 0
    photo=PhotoImage(file=f'img/{num}.gif')
    pic = Label(app,image=photo)

    pic.place(x=250,y=0,height=40,width=100)

app.mainloop()