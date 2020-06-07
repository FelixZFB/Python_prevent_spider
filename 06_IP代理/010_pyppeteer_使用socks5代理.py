# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/6/5 16:09
Desc:
'''
import asyncio
from pyppeteer import launch

proxy = '127.0.0.1:7891'



async def main():
    # 使用args参数传入，传入的是一个列表
    browser = await launch({'args': ['--proxy-server=socks5://' + proxy], 'headless': False})
    page = await browser.newPage()
    await page.goto('https://httpbin.org/get')
    print(await page.content())
    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())