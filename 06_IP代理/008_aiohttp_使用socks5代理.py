# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/6/5 15:54
Desc:
'''
import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector, ProxyType

# connector = ProxyConnector.from_url('socks5://127.0.0.1:7891')

connector = ProxyConnector(
    proxy_type=ProxyType.HTTP,
    host='127.0.0.1',
    port=7890,
    # username='user',
    # password='password',
    # rdns=True
)

async def main():
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get('https://httpbin.org/get') as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())