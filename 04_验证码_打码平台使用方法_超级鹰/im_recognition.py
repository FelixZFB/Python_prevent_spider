# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/6/29 10:07
Desc:
'''

import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chaojiying import Chaojiying

# 基本参数
# 要登录的网址：https://captcha3.scrape.cuiqingcai.com/
# 登录的用户名和密码，点击登录后就会弹出验证码图片
USERNAME = 'admin'
PASSWORD = 'admin'

# 超级鹰平台的用户名，密码
CHAOJIYING_USERNAME = 'xiashubai123'
CHAOJIYING_PASSWORD = 'zfb123456zfb'
# 个人软件ID(用户中心申请)，识别验证码类型，具体查看：https://www.chaojiying.com/price.html#table-item2
# 上面测试网站第一次登陆，是识别两个汉字的位置，依次点击，如果连续第二次登陆就会变成四个汉字
CHAOJIYING_SOFT_ID = 906127
CHAOJIYING_KIND = 9102  # 9102 点击两个相同的字,返回:x1,y1|x2,y2	题分(22)

# 先判断是否传入了用户名和密码
if not CHAOJIYING_USERNAME or not CHAOJIYING_PASSWORD:
    print('请先设置用户名和密码')
    exit(0)


class CrackCaptcha():

    # 初始化了浏览器对象和打码平台的操作对象
    def __init__(self):
        # 要登录的网址
        self.url = 'https://captcha3.scrape.cuiqingcai.com/'
        # 自动化浏览器
        self.browser = webdriver.Chrome()
        # 等待方法访问网址，超时时间20秒
        self.wait = WebDriverWait(self.browser, 20)
        self.username = USERNAME
        self.password = PASSWORD
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)

    # 打开网页，填写表单
    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)
        # 获取用户名和密码表单，填入用户名密码
        # wait显示等待方法访问，until判断元素是否存在，EC模块进行检验，参数传入检测类型和条件，检测不通过就抛出异常
        username = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
        password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        username.send_keys(self.username)
        password.send_keys(self.password)

    # 获取点击验证按钮
    def get_captcha_button(self):
        """
        获取初始验证按钮
        :return:
        """
        button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="button"]')))
        # 点击按钮
        button.click()
        return button

    # 获取验证码元素对象
    def get_captcha_element(self):
        """
        获取验证图片对象
        :return: 图片对象
        """
        # 超时等待使用方法具体查看Spider_scrapy_intensive_study的004笔记
        # 验证码图片加载出来，验证码图片位于img标签，class属性geetest_item_img
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'img.geetest_item_img')))
        # 验证码弹出窗口完整节点，div标签，class属性geetest_panel_box，
        # 获取整个弹出的验证码窗口部分，要包含着图片上部和底部的文字部分，文字要依次点击，后台要根据文字顺序返回坐标位置
        element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_panel_box')))
        print('成功获取验证码节点')
        # print(element)
        return element

    # 获取验证码图片（验证码弹窗）在浏览器窗口的位置
    def get_captcha_position(self):
        """
        获取验证码位置，整个验证码弹窗的位置
        :return: 验证码位置元组
        """
        # 获取验证码图片元素
        element = self.get_captcha_element()
        time.sleep(2)
        # 取出验证码图片的位置，使用location属性，左上角坐标位置xy坐标
        location = element.location
        print('验证码弹窗在浏览器窗口的位置(坐上角位置坐标):' + str(location))
        # size就是div标签大小(宽度和高度)，就是验证码图片的大小
        size = element.size
        print('验证码弹窗的尺寸:' + str(size))
        # 顶部就是y坐标，底部就用顶部加上高度，左边就是x坐标，右边就是左边加上宽度
        top, bottom, left, right = location['y'], location['y'] + size['height'] + size['height'], location['x'], location['x'] + size[
            'width']+ size['width']
        # 返回验证码图片四个边框位置
        return (top, bottom, left, right)

    # 网页截图保存方法，截取的是整个网页
    def get_screenshot(self):
        """
        获取网页截图方法
        :return: 截图对象，截取的是整个网页
        """
        # 注意，chrome浏览器必须先截屏浏览器窗口，然后再定位截取元素，火狐浏览器定位元素后可以直接截取元素
        # 火狐可以直接使用element.save_screenshot

        # 谷歌浏览器：
        # 1. chrome save_screenshot 截图，可以截取整个网页。
        # 2. 利用element的size和location属性，获取element在网页(浏览器窗口)中的位置。
        # 3. 这之后用PIL下Image中的crop方法截取元素。

        # 截图，
        screenshot = self.browser.get_screenshot_as_png()
        # 截图打开为字节文件，screenshot已经变成了Image下的方法，后面直接使用corp方法截取元素
        screenshot = Image.open(BytesIO(screenshot))
        # 将截图的字节文件保存为png图片，此处截取的是整个网页，即浏览器窗口
        screenshot.save('screenshot.png')
        # 返回截图的字节文件
        return screenshot

    # 根据验证码图片位置截图，然后保存为图片
    def get_captcha_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        # 获取验证码元素的位置
        top, bottom, left, right = self.get_captcha_position()
        print('验证码图片的位置:', top, bottom, left, right)
        # 调用截图方法
        screenshot = self.get_screenshot()
        # 利用element的size和location属性，获取element在网页中的位置,即验证码元素的位置
        # 用PIL下Image中的crop方法截取元素，根据验证码图片在浏览器窗口中位置进行截图
        captcha = screenshot.crop((left, top, right, bottom))
        # 保存截取的验证码图片
        captcha.save(name)
        return captcha

    # 传入图片给超级鹰后台识别,返回识别结果JSON 格式的字符串，如下，pic_str里面就是要点击文字的坐标位置（左上角坐标）
    # {'err_no': 0, 'err_str': 'OK', 'pic_id': '6002001380949200001', 'pic_str': '132,127|56,77', 'md5': '1f8e1d4bef8b11484cb1f1f34299865b'}
    def recognize_image(self):
        image = self.get_captcha_image()
        bytes_array = BytesIO()
        image.save(bytes_array, format='PNG')
        #  识别验证码
        result = self.chaojiying.post_pic(bytes_array.getvalue(), CHAOJIYING_KIND)
        # print(result)
        return result

    # 解析识别结果，解析出来位置坐标
    def get_points(self, captcha_result):
        """
        解析识别结果
        :param captcha_result: 识别结果
        :return: 转化后的结果
        """
        groups = captcha_result.get('pic_str').split('|')
        locations = [[int(number) for number in group.split(',')] for group in groups]
        return locations

    # 根据文字坐标位置，依次点击文字
    def touch_click_words(self, locations):
        """
        点击验证图片
        :param locations: 点击位置
        :return: None
        """
        for location in locations:
            ActionChains(self.browser).move_to_element_with_offset(self.get_captcha_element(), location[0], location[
                1]).click().perform()
        time.sleep(1)


if __name__ == '__main__':
    crack_captcha = CrackCaptcha()
    crack_captcha.open()
    # 打开网页后，填入表单，发送请求后相应需要时间，等待一会儿再点击按钮进行后续操作
    time.sleep(3)
    # 点击后的截图操作方法中已经使用了等待方法，不用手动设置等待时间
    crack_captcha.get_captcha_button()

    # 超级鹰后台识别
    captcha_result = crack_captcha.recognize_image()

    # 获取识别后的坐标位置，然后模拟点击
    locations = crack_captcha.get_points(captcha_result=captcha_result)
    crack_captcha.touch_click_words(locations=locations)


# 存在问题：
# 问题1：验证码弹窗获取宽度高度准确，获取的坐标位置，X位置不对，偏左了，Y位置正确
# 导致截图，截取了一部分弹窗左侧空白位置，右侧未截图完整
# 元素位置宽度和高度都取两倍，保证截图完整

# 运行结果：
# 成功获取验证码节点
# <selenium.webdriver.remote.webelement.WebElement (session="dfb3676b0cb4115886a67f701dce9775", element="0.6633065881478677-5")>
# 验证码弹窗在浏览器窗口的位置(坐上角位置坐标):{'x': 357, 'y': 132}
# 验证码弹窗的尺寸:{'height': 412, 'width': 322}
# 验证码图片的位置: 132 956 357 1001
# 成功获取验证码节点
# <selenium.webdriver.remote.webelement.WebElement (session="dfb3676b0cb4115886a67f701dce9775", element="0.6633065881478677-5")>
# 验证码弹窗在浏览器窗口的位置(坐上角位置坐标):{'x': 357, 'y': 132}
# 验证码弹窗的尺寸:{'height': 412, 'width': 322}
# 验证码图片的位置: 132 956 357 1001
# {'err_no': 0, 'err_str': 'OK', 'pic_id': '9109209234472700003', 'pic_str': '242,698|423,671', 'md5': '762c32355d30b15307ac9162f36a8c06'}
# 成功获取验证码节点
# <selenium.webdriver.remote.webelement.WebElement (session="dfb3676b0cb4115886a67f701dce9775", element="0.6633065881478677-5")>
# 成功获取验证码节点
# <selenium.webdriver.remote.webelement.WebElement (session="dfb3676b0cb4115886a67f701dce9775", element="0.6633065881478677-5")>
#
# Process finished with exit code 0

