from lxml import etree  #html解析器
import  requests  #源码获取器
from chardet import detect

print('请从‘xbiquge.so’搜索')
###询问基本数据
num = input('请输入书籍编号：')  #书籍号
num1 = int(input('请输入第一集的编号：'))  #第一集
num2 = int(input('请输入最后一集的编号:'))  #最后一集
name = input('请输入书籍名称：')  #书名

###定义系统数据
x = 0  #成功数量
y = 0  #无法下载
list1 = ['以下链接无法下载,请手动复制']

###核心程序
while num1 <= num2:
    url=f'https://www.xbiquge.so/book/{num}/{num1}.html'
    resp=requests.get(url)  #获取源码


    try:
        #解析源码
        ecoding=detect(resp.content).get('encoding')
        html=resp.content.decode(ecoding)
        tree=etree.HTML(html)

        #获取核心数据
        a=tree.xpath('/html/body/div[1]/div[2]/div/div[2]/h1/text()')  #a是标题(list)
        b=tree.xpath('/html/body/div[1]/div[2]/div/div[4]/text()')  #b是内容(list)

        #写入文本
        file1 = open(f'{name}.txt','a',encoding='utf8')  #创建文本文件

        
        for a2 in a:
            file1.write(str(a2)+'\n')

        for b2 in b:
            file1.write(str(b2)+'\n')         

        file1.close()

        x += 1

    except:  
        list1.append(f'https://www.xbiquge.so/book/{num}/{num1}.html')  #写入无法下载的
        y += 1
        print(f"'https://www.xbiquge.so/book/{num}/{num1}.html'无法下载")
    
    print(f'已下载{x}集')

    num1 += 1

###输出无法下载链接
for cannot in list1:
    print(cannot)

input('按‘回车’键退出')