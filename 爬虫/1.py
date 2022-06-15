import requests

url = 'https://www.baidu.com'  #需要访问'https://www.baidu.com'
resp=requests.get(url)  #请求url
print(resp)  #打印请求结果的状态码(状态码“200”正常)
print(resp.content)  #打印请求到的网页源码