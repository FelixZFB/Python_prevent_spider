# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/10 16:07
Desc:
'''
# http://www.porters.vip/verify/sign/
# 上述网址，点击查看详情，查看network
# 下面网址就是动态加密生成的，直接复制去请求是无效的，网址有多个参数还有时间戳，直接浏览器再次去请求就是无效的
# http://www.porters.vip/verify/sign/fet?actions=31288&tim=1583827827&randstr=JUBMB&sign=1f46e27e48caacc155fbf9afde6bbbc0
# 动态加密请求，就是需要破解动态网址是如何生成的

from time import time
from random import randint, sample
import hashlib
import requests

def hex5(value):
    # 使用 MD5 加密值并返回加密后的字符串
    manipulator = hashlib.md5()
    manipulator.update(value.encode('utf-8'))
    return manipulator.hexdigest()

def uri():
    # 生成1-9随机的5个数
    action = "".join([str(randint(1, 9)) for _ in range(5)])
    # 生成当前的时间戳
    tim = round(time())
    # 生成5个随机的大写字母
    rand_str = "".join(sample([chr(_) for _ in range(65, 91)], 5))
    # 上面三个参数拼接后进行MD5加密
    value = action + str(tim) + rand_str
    hex_str = hex5(value)

    args = '?actions=' + action + '&tim=' + str(tim) + '&randstr=' + rand_str + '&sign=' + hex_str
    return args

def get():
    url = "http://www.porters.vip/verify/sign/fet" + uri()
    print(url)
    res = requests.get(url)
    print(res.status_code)
    print(res.text)

if __name__ == '__main__':
    uri()
    get()

