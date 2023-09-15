
import requests
import re

url = 'https://top.baidu.com/board?tab=realtime'
r = requests.get(url)
seqfind = re.compile('<div class="c-single-text-ellipsis">  (.*?) <.*?>', re.S)
titles = re.findall(seqfind, r.text) # findall函数输出一个表格
# print(titles)
print("百度热搜榜: ")
for i in titles:
    if titles.index(i) > 0:
        print(titles.index(i), end=":\t\b\b\b\b")
        print(i)
    else:
        print("Top", end=":\t\b\b\b\b")
        print(i)

# 热搜标题HTML代码如下
# <div class="c-single-text-ellipsis">  加快构建新发展格局 <!--39--></div>
