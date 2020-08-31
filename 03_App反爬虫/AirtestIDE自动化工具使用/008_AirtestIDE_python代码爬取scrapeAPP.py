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

# 导入包
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# 要抓取的 app 名称
PACKAGE_NAME = 'com.goldze.mvvmhabit'
# 声明了 AndroidUiautomationPoco 对象，赋值为 poco，即获得了 App 的操作句柄
poco = AndroidUiautomationPoco()
# 设备唤醒，手机可能处于息屏状态
poco.device.wake()

# 调用了 stop_app 和 start_app 并传入 app 包名实现了 App 的重启，确保是从头开始抓取的。
stop_app(PACKAGE_NAME)
start_app(PACKAGE_NAME)

auto_setup(__file__)

# 获取屏幕宽度高度
screenWidth, screenHeight = poco.get_screen_size()
# 定义一个列表，用于保存电影名称
viewed = []
current_count, last_count = len(viewed), len(viewed)

# 定义了一个无限循环，提取的是 android.support.v7.widget.RecyclerView
# 里面的 android.widget.LinearLayout 子节点，会一次性命中多个
while True:
    last_count = len(viewed)
    result = poco('android.support.v7.widget.RecyclerView').child('android.widget.LinearLayout')
    result.wait(timeout=10)

    #  for 循环遍历了每个节点，获取到了其中的 android.widget.TextView 节点，
    #  并用 get_text 提取了文本值，保存到 viewed 变量里面并去重，电影名称
    for item in result:
        text_view = item.child(type='android.widget.TextView')
        if not text_view.exists():
            continue
        name = text_view.get_text()
        if not name in viewed:
            viewed.append(name)
            print('名称', name)
    current_count = len(viewed)

    # 遍历完成一遍之后，调用 swipe 方法滑动手机，进行上拉加载，同时滑动完毕之后等待一段时间
    print('开始滑动')
    # 传入滑动区域，就是屏幕的一个截图区域，向上滑动Y轴为负值，
    swipe((screenWidth * 0.5, screenHeight * 0.7), vector=[0, -0.8], duration=3)
    print('滑动结束')
    sleep(5)

    # 重复以上步骤，直到 viewed 的数量不再变化，终止抓取
    if current_count == last_count:
        print('数量不再有变化，抓取结束')
        break
