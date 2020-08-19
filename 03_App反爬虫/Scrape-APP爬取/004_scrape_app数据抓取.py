# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/8/19 10:53
Desc:
'''

import requests

BASE_URL = 'https://dynamic1.scrape.cuiqingcai.com/api/movie?offset={offset}&limit=10'
for i in range(0, 10):
    offset = i * 10
    url = BASE_URL.format(offset=offset)
    data = requests.get(url).json()
    print('data', data)

# 注意：
# Charles 中已经启用了 SSL代理 ，该代码要运行，需要关闭Charles软件或者关闭 Charles里面的SSL代理设置
# 不然直接运行会报错SSL相关错误
