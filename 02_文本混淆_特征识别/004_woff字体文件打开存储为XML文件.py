# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/14 16:23
Desc:
'''
from fontTools.ttLib import TTFont

# 打开当前目录的woff字体文件
font = TTFont('movie.woff')
# 字体文件另存为XML文件
font.saveXML('movie.xml')