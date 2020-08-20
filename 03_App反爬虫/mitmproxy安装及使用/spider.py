# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/8/20 11:26
Desc:
'''


# def response(flow):
#     # 构造 mitmproxy 的响应
#     response = flow.response
#     info = ctx.log.info
#     info(str(response.status_code))
#     info(str(response.headers))
#     info(str(response.cookies))
#     info(str(response.text))

import json
from mitmproxy import ctx

def response(flow):
    response = flow.response
    if response.status_code != 200:
        return
    data = json.loads(str(response.text))
    for item in data.get('results'):
        name = item.get('name')
        with open(f'{name}.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(item, indent=2, ensure_ascii=False))

