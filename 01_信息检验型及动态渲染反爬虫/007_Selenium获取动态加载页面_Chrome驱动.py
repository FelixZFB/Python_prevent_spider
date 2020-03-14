# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/11 15:41
Desc:
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def main():
    # 设置无界面浏览器,取消该设置，浏览器会自动打开操作
    options = Options()
    # options.add_argument('-headless')

    # 创建一个无界面的浏览器实例
    driver = webdriver.Chrome(options=options)

    # 访问指定网站
    url = 'http://www.porters.vip/verify/sign/'
    driver.get(url)

    # 查看网页的标题
    print("网页Title: {0}".format(driver.title))

    # 定位元素，并点击按钮
    # driver.find_element_by_id('fetch_button').click()  # 使用id进行定位
    driver.find_element_by_css_selector('#fetch_button').click()  # 使用css选择器定位


    # 定位元素，取出文本内容
    # res = driver.find_element_by_id('content').text
    res = driver.find_element_by_css_selector('#content').text
    print(res)

    # 关闭浏览器
    driver.close()

if __name__ == '__main__':
    main()