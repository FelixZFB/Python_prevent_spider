# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/20 10:42
Desc:
'''
import time
from selenium import webdriver


browser = webdriver.Chrome()
# 驱动Chrome浏览器打开滑动验证码示例页面
browser.get('http://www.porters.vip/captcha/jigsawCanvas.html')

# 定位滑块
jigsawCircle = browser.find_element_by_css_selector('#jigsawCircle')
# 定位背景图片
jigsawCanvas = browser.find_element_by_css_selector('#jigsawCanvas')
jigsawCanvas.screenshot('before.png')
action = webdriver.ActionChains(browser)
# 点击并保持不松开
action.click_and_hold(jigsawCircle).perform()
# 执行js隐藏圆角矩形的HTML代码
scripts = """
var missblock = document.getElementById('missblock');
missblock.style['visibility'] = 'hidden';
"""
browser.execute_script(scripts)
# 再次截图
jigsawCanvas.screenshot('after.png')


time.sleep(5)
# 对比缺口图前后，比较像素不同，找出缺口位置
from PIL import Image
from PIL import ImageChops

# 打开待比对的图片
image_a = Image.open('after.png')
image_b = Image.open('before.png')

# 使用ImageChops模块中的difference方法比对图片像素的不同
diff = ImageChops.difference(image_b, image_a)
# 获取图片差异位置的坐标，返回值就是缺口位置上下左右的坐标数值(图片左下角为原点)，单位就是像素px
diff_position = diff.getbbox()
print(diff_position)


# 取出缺口的左边的数值
position_x = diff_position[0]
action.move_by_offset(int(position_x)-10, 0)  # 设置移动距离，要移动小图离图形左边有10px距离
action.release().perform()  # 松开鼠标
browser.close()