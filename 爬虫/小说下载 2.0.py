from lxml import etree  #html解析器
import  requests  #源码获取器
from chardet import detect
from bs4 import BeautifulSoup
import re  #正则表达式匹配

###询问基本数据
# num = input('请输入书籍编号：')  #书籍号

name = input('请输入书籍名称：')  #书名
file1 = open(f'{name}.txt','a',encoding='utf8')  #创建文本文件

###定义系统数据
x = 0  #成功数量
y = 0  #无法下载
list_url = []
list_n = ['以下链接无法下载']
num = 55182
###核心程序

url=f'https://www.xbiquge.so/book/{num}'
resp=requests.get(url)  #获取源码

lxml=BeautifulSoup(resp.content,'lxml')
a_list=lxml.find_all('a')


for a in a_list:
    href=a.get('href')
    aaa = re.findall('.*?.html',href)

    for html in aaa:
        print(html)
        list_url.append(html)

del list_url[:13]
print(list_url)


###25

resp=""
for url2 in list_url:
    while resp != "<Response [200]>":
        try:
            url=f'https://www.xbiquge.so/book/{num}/{url2}'
            resp=requests.get(url)
            print(resp)

            #解析源码
            ecoding=detect(resp.content).get('encoding')
            html=resp.content.decode(ecoding)
            tree=etree.HTML(html)  #把字符串解析为html文档

            #获取核心数据
            a=tree.xpath('/html/body/div[1]/div[2]/div/div[2]/h1/text()')  #a是标题(list)
            b=tree.xpath('/html/body/div[1]/div[2]/div/div[4]/text()')  #b是内容(list)

            #写入文本           
            for a2 in a:
                file1.write(str(a2)+'\n')

            for b2 in b:
                file1.write(str(b2)+'\n')         


        except:  
            list_n.append(f'https://www.xbiquge.so/book/{num}/{url2}')  #写入无法下载的
            y += 1
            print(f"'https://www.xbiquge.so/book/{num}/{url2}' 第{y}次 无法下载")
        print(f'已下载{x}集')
        x += 1

    
file1.close()

for xxx in list_n:
    print(xxx)


input('按‘回车’键退出')