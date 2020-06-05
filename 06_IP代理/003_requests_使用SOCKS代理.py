# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/6/5 15:34
Desc:
'''
import requests

proxy='127.0.0.1:7891'

proxies={
    'http':'socks5://'+proxy,
    'https':'socks5://'+proxy,
}

try:
    response=requests.get('https://httpbin.org/get', proxies=proxies)
    print(response.text)
    print(response.status_code)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)