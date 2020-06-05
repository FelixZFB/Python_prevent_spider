# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/6/5 11:45
Desc:
'''
import requests

proxy='127.0.0.1:7890'

proxies={
    'http':'http://'+proxy,
    'https':'https://'+proxy,
}

try:
    response=requests.get('https://httpbin.org/get', proxies=proxies)
    print(response.text)
    print(response.status_code)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)

# 代理需要认证，同样在代理的前面加上用户名密码即可，代理的写法就变成如下所示：
# 复制proxy = 'username:password@127.0.0.1:7890'