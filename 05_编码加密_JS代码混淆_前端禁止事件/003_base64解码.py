# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/24 9:14
Desc:
'''
from base64 import b64decode

# base64编码后的字符串
code = ['d3d3Lmh1YXdlaS5jb20=', 'd3d3Lmp1ZWppbi5pbQ==']

for c in code:
    # 先解码为字节然后解码为utf-8字符串
    string = b64decode(c).decode('utf8')
    print(string)