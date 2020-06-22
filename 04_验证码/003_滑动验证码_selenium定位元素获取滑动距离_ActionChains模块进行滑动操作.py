# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/19 16:13
Desc:
'''
from selenium import webdriver
import re

browser = webdriver.Chrome()
# 驱动Chrome浏览器打开滑动验证码示例页面
browser.get('http://www.porters.vip/captcha/sliders.html')
# 定位滑轨,获取滑轨宽度属性的值
track = browser.find_element_by_css_selector('.tracks')
track_width = track.value_of_css_property('width')
track_width = int((re.findall('\d+', track_width))[0]) # 属性的值有单位px，只提取数字，然后列表中取出
# 定位滑块,获取滑块宽度属性的值
hover = browser.find_element_by_css_selector('.hover')
hover_width = hover.value_of_css_property('width')
hover_width = int((re.findall('\d+', hover_width))[0])

# 计算滑动距离，滑轨宽度减去滑块宽度
slide_distance = track_width - hover_width

# 滑动滑块
action = webdriver.ActionChains(browser)
action.click_and_hold(hover).perform()  # 点击并保持不松开
action.move_by_offset(slide_distance, 0)  # 设置滑动距离，横向距离为计算值，纵向距离0px
action.release().perform()  # 松开鼠标