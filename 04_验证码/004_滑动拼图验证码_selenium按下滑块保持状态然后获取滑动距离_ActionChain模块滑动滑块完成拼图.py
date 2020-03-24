# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/20 10:16
Desc:
'''

from selenium import webdriver
browser = webdriver.Chrome()
# 驱动Chrome浏览器打开滑动验证码示例页面
browser.get('http://www.porters.vip/captcha/jigsaw.html')
# 定位滑块
jigsawCircle = browser.find_element_by_css_selector('#jigsawCircle')
action = webdriver.ActionChains(browser)
# 点击滑块并保持不松开，此时页面源码已经发生了变化
# 滑块缺口处的style样式都有了left值，通过两个left的差值确定滑动距离
action.click_and_hold(jigsawCircle).perform()
# 返回当前页面的html代码
html = browser.page_source


# 003案例是样式是放在css标签里面，直接使用的selenium获取css属性的值
# 此案例样式是放在标签的style里面，需要先保存页面，然后页面使用css选择器定位后提取left的值
import re
from parsel import Selector
sel = Selector(html)
# 获取圆角矩形和缺口的CSS样式
mbk_style = sel.css('#missblock::attr("style")').get()
tbk_style = sel.css('#targetblock::attr("style")').get()
# 编写用于从CSS样式中提取left属性值的匿名函数，提取出数字,缺口的left值可能是小数
# 提取的数字列表join为一个字符串，实际结果就是数字的字符串
extract = lambda x: ''.join(re.findall('left: (\d+|\d+\.\d+)px', x))
# 调用匿名函数获取CSS样式中的left属性值
mbk_left = extract(mbk_style)   # 图片left值
tbk_left = extract(tbk_style)   # 缺口left值
print(mbk_left, tbk_left)
# 计算当前拼图验证码滑块所需移动的距离
distance = float(tbk_left) - float(mbk_left)


# 移动滑块，完成拼图验证
action.move_by_offset(distance, 0)  # 设置滑动距离
action.release().perform()  # 松开鼠标
browser.close()