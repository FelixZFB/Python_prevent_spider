# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/6/5 15:45
Desc:
'''
from selenium import webdriver

proxy = '127.0.0.1:7890'
options = webdriver.ChromeOptions()

# 添加一个代理参数，http修改为socks5即可
options.add_argument('--proxy-server=socks5://' + proxy)
# 创建浏览器对象时候传入参数即可
browser = webdriver.Chrome(options=options)

browser.get('https://httpbin.org/get')
print(browser.page_source)
browser.close()