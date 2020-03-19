# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/19 15:59
Desc:
'''
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
from PIL import Image
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
    url = 'http://www.porters.vip/captcha/words.html'
    driver.get(url)
    # 查看网页的标题
    print("网页Title: {0}".format(driver.title))
    # 定位元素
    # driver.find_element_by_id('wordsCanvas')  # 使用id进行定位
    mathes = driver.find_element_by_css_selector('#wordsCanvas')  # 使用css选择器定位
    # 截图元素(验证码部分)保存到本地
    mathes.screenshot('words.png')
    # 关闭浏览器
    driver.close()

# 图片进行二值化处理
def handler(grays, threshold=160):
    """对灰度图片进行二值化处理
    默认阈值为160，可根据实际情况调整
    """
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    anti = grays.point(table, '1')
    return anti

# 打开保存的验证码图片，然后识别为文字
def image_to_string():
    # 保存在本地的验证码图片路径
    image = path.join(path.dirname(path.abspath(__file__)), 'words.png')
    # 图片灰度处理
    gray = Image.open(image).convert('L')
    # 图片二值化处理
    image = handler(gray)
    image.show()
    # 使用pytesseract库识别图中文字
    strings = pytesseract.image_to_string(image)
    print(strings)

# 缺点：pytesseract识别率较低，识别不出来就没有任何结果
# 即使进行二值化和灰度处理，很多还是无法识别
# 使用腾讯云的ocr识别，还是有些无法识别
save_image()
time.sleep(8)
image_to_string()



