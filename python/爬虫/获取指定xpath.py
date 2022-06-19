from lxml import etree  #html解析器
import  requests  #源码获取器
from chardet import detect

url=f'https://www.baidu.com'
resp=requests.get(url)  #获取源码

ecoding=detect(resp.content).get('encoding')
html=resp.content.decode(ecoding)
tree=etree.HTML(html)

#获取核心数据
a=tree.xpath('')  #填入xpath路径