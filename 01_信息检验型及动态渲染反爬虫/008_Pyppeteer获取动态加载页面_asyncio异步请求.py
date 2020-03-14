# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/11 16:06
Desc:
'''

import asyncio
from pyppeteer import launch

async def main():
    # 初始化浏览器对象
    browser = await launch()
    # 在浏览器上下文中创建新的页面
    page = await browser.newPage()
    # 打开目标网址
    url = 'http://www.porters.vip/verify/sign/'
    await page.goto(url)
    # 点击指定按钮
    await page.click('#fetch_button') # 使用css选择器语法进行定位
    # 读取页面指定位置的文本
    res = await page.xpath('//*[@id="content"]')
    text = await (await res[0].getProperty('textContent')).jsonValue()
    print(text)
    # 关闭浏览器对象
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())