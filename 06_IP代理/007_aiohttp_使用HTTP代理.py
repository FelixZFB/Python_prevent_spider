# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/6/5 15:51
Desc:
'''
import asyncio
import aiohttp

proxy = 'http://127.0.0.1:7890'

async def main():
    async with aiohttp.ClientSession() as session:
        # 直接传入代理参数即可
        async with session.get('https://httpbin.org/get', proxy=proxy) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

# 代理有用户名密码，像 requests 一样，把 proxy 修改为如下内容：
# proxy = 'http://username:password@127.0.0.1:7890'