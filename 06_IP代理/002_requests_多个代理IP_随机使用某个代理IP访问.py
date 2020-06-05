# -*- coding: utf-8 -*-

#导入random，对ip池随机筛选
# 多ip代理模式
import requests
import random

proxy = [
{
    'http': 'http://61.135.217.7:80',
    'https': 'http://61.135.217.7:80',
    },
{
        'http': 'http://118.114.77.47:8080',
        'https': 'http://118.114.77.47:8080',
    },
{
        'http': 'http://112.114.31.177:808',
        'https': 'http://112.114.31.177:808',
    },
{
        'http': 'http://183.159.92.117:18118',
        'https': 'http://183.159.92.117:18118',
    },
{
        'http': 'http://110.73.10.186:8123',
        'https': 'http://110.73.10.186:8123',
    },
]

url = 'https://www.baidu.com/'

response = requests.get(url, proxies=random.choice(proxy))

print(response.status_code)
print(response.headers)