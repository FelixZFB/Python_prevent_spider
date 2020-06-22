# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/19 15:09
Desc:
'''
import pytesseract
import time
import re
from os import path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 将验证码部分截图保存下来
def save_image():
    # 设置无界面浏览器,取消该设置，浏览器会自动打开操作
    options = Options()
    # options.add_argument('-headless')
    # 创建一个无界面的浏览器实例
    driver = webdriver.Chrome(options=options)
    # 访问指定网站
    url = 'http://www.porters.vip/captcha/mathes.html'
    driver.get(url)
    # 查看网页的标题
    print("网页Title: {0}".format(driver.title))
    # 定位元素
    # driver.find_element_by_id('matchesCanvas')  # 使用id进行定位
    mathes = driver.find_element_by_css_selector('#matchesCanvas')  # 使用css选择器定位
    # 截图元素(验证码部分)保存到本地
    mathes.screenshot('mathes.png')
    # 关闭浏览器
    driver.close()

# 打开保存的验证码图片，然后识别为文字
def image_to_string():
    # 保存在本地的验证码图片路径，使用path进行转换
    image = path.join(path.dirname(path.abspath(__file__)), 'mathes.png')
    # 使用pytesseract库识别图中文字
    strings = pytesseract.image_to_string(image)
    print(strings)
    # 提取所有的数字
    string = re.findall('\d+', strings)
    # 提取计算符号
    operator = re.findall('[+|\-|\*]', strings)
    print(string, operator)

    # 根据计算符号，转换为int类型后进行计算
    if operator[0] == '+':
        return int(string[0]) + int(string[1])
    if operator[0] == '-':
        return int(string[0]) - int(string[1])
    if operator[0] == '*':
        return int(string[0]) * int(string[1])


# 缺点：pytesseract识别率较低，有时候图片识别到字符串会出错
save_image()
time.sleep(5)
print(image_to_string())



