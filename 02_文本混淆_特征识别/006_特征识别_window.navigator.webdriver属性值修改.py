# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/16 16:17
Desc:
'''

from selenium.webdriver import Chrome
import time

browser = Chrome()
browser.get('http://www.porters.vip/features/webdriver.html')
# 编写修改navigator.webdriver值的JavaScript代码
script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
# 浏览器运行JavaScript代码，将属性值修改为false
browser.execute_script(script)
time.sleep(1)
# 定位按钮并点击
browser.find_element_by_css_selector('.btn.btn-primary.btn-lg').click()
# 定位到文章内容元素
elements = browser.find_element_by_css_selector('#content')
time.sleep(1)
# 打印文章内容
print(elements.text)
# 关闭浏览器
browser.close()