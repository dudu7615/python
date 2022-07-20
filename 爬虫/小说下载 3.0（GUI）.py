from lxml import etree  #html解析器
import  requests  #源码获取器
from chardet import detect
from bs4 import BeautifulSoup
import re  #正则表达式匹配
from tkinter import *


###核心程序 47179
def main():
    list_url = []
    num = book.get()

    file1 = open('new book.txt','a',encoding='utf8')  #创建文本文件

    url=f'https://www.biqugee.com/book/{num}/'
    resp=requests.get(url)  #获取源码

    lxml=BeautifulSoup(resp.content,'lxml')
    a_list=lxml.find_all('a')

    for a in a_list:
        href=a.get('href')
        aaa = re.findall('.*?.html',href)

        for html in aaa:
            print(html)
            list_url.append(html)

    del list_url[:2]
    print(list_url)

    x = 0  # 切换label
    x1 = 0  #总数
    x2 = 0  # 成功
    x3 = 0  # 失败
    for url2 in list_url:
        x1 += 1
        if x < 5:
            x+=1
        else:
            x = 1

        try:
            url1=f'https://www.biqugee.com{url2}'
            resp=requests.get(url1)
            print(resp)

            #解析源码
            ecoding=detect(resp.content).get('encoding')
            html=resp.content.decode(ecoding)
            tree=etree.HTML(html)  #把字符串解析为html文档

            #获取核心数据
            tittle_0 = tree.xpath('/html/body/div/div[5]/div/div[2]/h1/text()')  #a是标题(list)
            text_0 = tree.xpath('/html/body/div/div[5]/div/div[3]/text()')  #b是内容(list)

            #写入文本           
            for tittle in tittle_0:
                file1.write(str(tittle)+'\n')

            for text in text_0:
                file1.write(str(text)+'\n')  

            if x==1:
                down_label1 = Label(app,text=f"第{x1}集\n'https://www.biqugee.com{url2}' 正常下载",fg="green",font=("微软雅黑",11))
                down_label1.place(x=10,y=50,height=50,width=480)
                app.update()
            elif x==2:
                down_label2 = Label(app,text=f"第{x1}集\n'https://www.biqugee.com{url2}' 正常下载",fg="green",font=("微软雅黑",11))
                down_label2.place(x=10,y=100,height=50,width=480)
                app.update()
            elif x==3:
                down_label3 = Label(app,text=f"第{x1}集\n'https://www.biqugee.com{url2}' 正常下载",fg="green",font=("微软雅黑",11))
                down_label3.place(x=10,y=150,height=50,width=480)
                app.update()
            elif x==4:
                down_label4 = Label(app,text=f"第{x1}集\n'https://www.biqugee.com{url2}' 正常下载",fg="green",font=("微软雅黑",11))
                down_label4.place(x=10,y=200,height=50,width=480)
                app.update()
            elif x==5:
                down_label5 = Label(app,text=f"第{x1}集\n'https://www.biqugee.com{url2}' 正常下载",fg="green",font=("微软雅黑",11))
                down_label5.place(x=10,y=250,height=50,width=480)
                app.update()

            x2 += 1
        except:
            if x==1:
                down_label1 = Label(app,text=f"第{x1}集\n'https://www.biqugee.com{url2}' 无法下载",fg="red",font=("微软雅黑",11))
                down_label1.place(x=10,y=50,height=50,width=480)
                app.update()
            elif x==2:
                down_label2 = Label(app,text=f"第{x1}集\n'https://www.biqugee.com{url2}' 无法下载 ",fg="red",font=("微软雅黑",11))
                down_label2.place(x=10,y=100,height=50,width=480)
                app.update()
            elif x==3:
                down_label3 = Label(app,text=f"第{x1}集\n'https://www.biqugee.com{url2}' 无法下载",fg="red",font=("微软雅黑",11))
                down_label3.place(x=10,y=150,height=50,width=480)
                app.update()
            elif x==4:
                down_label4 = Label(app,text=f"第{x1}集\n'https://www.biqugee.com{url2}' 无法下载",fg="red",font=("微软雅黑",11))
                down_label4.place(x=10,y=200,height=50,width=480)
                app.update()
            elif x==5:
                down_label5 = Label(app,text=f"第{x1}集\n'https://www.biqugee.com{url2}' 无法下载",fg="red",font=("微软雅黑",11))
                down_label5.place(x=10,y=250,height=50,width=480)
                app.update()

            x3+=1

    file1.close()
    print('finish')
    finish = Label(app,text=f"共尝试了{x1}集\n其中{x2}集成功下载\n{x3}集无法下载",font=("微软雅黑",20))
    finish.place(x=10,y=50,height=250,width=480)

app = Tk()
app.geometry('500x300')
app.title("小说下载")

num0 = StringVar()
num0.set('请输入书籍号')

book = Entry(app,textvariable=num0,font=("微软雅黑",11))
down = Button(app,text="开始下载",font=("微软雅黑",11),command=main)

book.place(x=150,y=0,height=40,width=100)
down.place(x=250,y=0,height=40,width=100)

app.mainloop()