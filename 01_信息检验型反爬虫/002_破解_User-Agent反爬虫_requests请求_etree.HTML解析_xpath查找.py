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

# 添加请求头信息，里面加入浏览器信息,用于伪装身份信息
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400"}

res = requests.get(url=url, headers=headers)
# 打印请求状态码
print(res.status_code)
# 如果请求的状态码为200，则继续
if res.status_code == 200:
    html = etree.HTML(res.text, etree.HTMLParser())
    # 普通xpath解析得到的结果就是所有内容的一个列表，对比003中的Selector解析结果
    title = html.xpath('//li[@class="list-group-item"]/text()')
    print(title)
else:
    print('This request is fail.')