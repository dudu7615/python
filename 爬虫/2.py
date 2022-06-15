import requests
from bs4 import BeautifulSoup

url = 'https://www.baidu.com'
resp=requests.get(url) #请求百度首页

bsobj=BeautifulSoup(resp.content,'lxml') #将网页源码构造成BeautifulSoup对象，方便操作
a_list=bsobj.find_all('a') #获取网页中的所有a标签对象
for a in a_list:  #从“a_list”中每次赋值给“a”
    print(a.get('href')) #打印a标签对象的href(链接)属性，即这个对象指向的链接地址