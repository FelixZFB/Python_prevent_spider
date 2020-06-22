# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/19 15:46
Desc:
'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()  # 最大化窗口
driver.get("https://www.autohome.com.cn")

driver.save_screenshot('capture.png')  # 截取浏览器窗口保存为图片

ele = driver.find_element_by_id('s4612')
ele.screenshot('ele.png')  # 元素截图，找到元素，截取元素部分

driver.close()