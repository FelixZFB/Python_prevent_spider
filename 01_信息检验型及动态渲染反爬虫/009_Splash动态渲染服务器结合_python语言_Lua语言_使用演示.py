# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/11 22:29
Desc:
'''
import requests
import json

# Splash的API接口
api_url = 'http://www.porters.vip:8050/execute'

# Splash里面需要执行的命令
# 脚本是Lua语言，实际和python很多还是比较类似
script = """
    function main(splash)
    splash:go('http://www.porters.vip/verify/sign/')
    local butt = splash:select('#fetch_button')
    butt:mouse_click()
    content = splash:select('#content'):text()
    return {
        results = content
    }
    end
"""

# 设置请求头
header = {'content-type': 'application/json'}
# 按照splash的规定格式提交命令
data = json.dumps({'lua_source': script}) # 字典数据转换为json格式数据
# 向splash的api接口发出请求，并携带上请求头和命令参数data
res = requests.post(api_url, data=data, headers=header)
# 打印出返回结果的json数据，res.json()表示返回响应经过json编码的内容，结果类型是一个python字典
print(res.json())
print(type(res.json()))

