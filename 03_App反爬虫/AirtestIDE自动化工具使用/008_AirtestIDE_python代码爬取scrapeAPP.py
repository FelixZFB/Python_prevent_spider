# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/8/24 16:47
Desc:
'''

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

PACKAGE_NAME = 'com.goldze.mvvmhabit'
poco = AndroidUiautomationPoco()
poco.device.wake()
stop_app(PACKAGE_NAME)
start_app(PACKAGE_NAME)
auto_setup(__file__)
screenWidth, screenHeight = poco.get_screen_size()
viewed = []
current_count, last_count = len(viewed), len(viewed)
while True:
    last_count = len(viewed)
    result = poco('android.support.v7.widget.RecyclerView').child('android.widget.LinearLayout')
    result.wait(timeout=10)
    for item in result:
        text_view = item.child(type='android.widget.TextView')
        if not text_view.exists():
            continue
        name = text_view.get_text()
        if not name in viewed:
            viewed.append(name)
            print('名称', name)
    current_count = len(viewed)
    print('开始滑动')
    swipe((screenWidth * 0.5, screenHeight * 0.7), vector=[0, -0.8], duration=3)
    print('滑动结束')
    sleep(5)

    if current_count == last_count:
        print('数量不再有变化，抓取结束')
        break
