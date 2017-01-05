# coding=utf-8
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

url = "http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C3%C0%C5%AE%CD%BC%C6%AC&ala=1&fr=ala&alatpl=cover&pos=0"

html = urllib2.urlopen(url)
# obj 返回的是一个BeautifulSoup 一个数据对象
obj = BeautifulSoup(html, 'html.parser')
#先定义初始值
index = 0
#正则匹配查找
urls = re.findall(r'"objURL":"(.*?)"', str(obj))
print urls

for url in urls:
    if index <= 10:
        urllib.urlretrieve(url, 'pic' + str(index) + '.jpg')
        # urlretrieve() 方法直接将远程数据下载到本地
        # 第一个参数 遍历的 url 链接 ，第二个参数是 文件名称。

        index += 1
    else:
        print '下载完成'
        break

if __name__ == '__main__':
    pass
