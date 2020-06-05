# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/9 21:53
Desc:
'''
import requests
from lxml import etree

# 一个具有User-Agent用户识别的网址
url = "http://www.porters.vip/verify/uas/index.html"
res = requests.get(url)
# 打印请求状态码
print(res.status_code)
# 如果请求的状态码为200，则继续
if res.status_code == 200:
    html = etree.HTML(res.text, etree.HTMLParser())
    title = html.xpath('//li[@class="list-group-item"/text()]')
    print(title)
else:
    print('This request is fail.')