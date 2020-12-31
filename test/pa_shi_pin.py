import requests
from bs4 import BeautifulSoup
response = requests.get(file='file:///Users/liyan/Downloads/untitled.html')
response.encoding = response.apparent_encoding  #返回什么就打印什么，编码一般是utf-8
soup = BeautifulSoup(response.text,features='html.parser')   #把文本转换成对象，features代表以什么引擎进行转换
target = soup.find(id='titlespan noScore')  #找id=？的标签
# print(target)
li_list = target.find_all('li')  #find只找到第一个li，列表类型，没有find方法，但是列表里的元素有，是对象
# print(li_list)  #找到所有li，是一个列表
for i in li_list:
    a = i.find('span')    #寻找a标签，并拿到a标签下内容
    print(a)