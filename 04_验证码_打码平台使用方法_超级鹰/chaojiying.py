# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
GihHub: https://github.com/FelixZFB
Date: 2020/6/29 9:10
Desc:
'''
import requests
from hashlib import md5

# 定义超级鹰接口类，里面定义一些方法
class Chaojiying(object):

    # 构造函数（初始化方法）接收三个参数，分别是超级鹰的用户名、密码以及软件 ID
    def __init__(self, username, password, soft_id):
        self.uername = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id # 软件id在用户中心，左侧菜单栏底部，自己生成一个ID号(填入软件名及说明，生成一个ID)
        # 打码平台的用户名，密码，软件ID
        self.base_params = {
            'user': self.uername,
            'pass2': self.password,
            'softid': self.soft_id,
        }

        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'
        }

    # 传入图片对象和验证码类型的代号。该方法会将图片对象和相关信息发给超级鹰的后台进行识别，然后将识别成功的 JSON 返回。
    def post_pic(self, im, codetype):
        '''
        :param im: 图片字节
        :param codetype: 验证码类型(代号) 参考：http://www.chaojiying.com/price.html
        :return: 识别后的json数据
        '''
        params = {
            'codetype': codetype
        }
        # 内置update方法加入上面的base_params参数
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        # 传入验证码图片，请求，返回识别数据
        r = requests.post(
            'http://upload.chaojiying.net/Upload/Processing.php',
            data=params,
            files=files,
            headers = self.headers
        )

        # requests.post结果返回成json格式数据
        return r.json()

    # 发生错误时的回调。如果验证码识别错误，调用此方法会返回相应的题分
    def report_error(self, im_id):
        '''
        :param im_id: 报错验证码图片的ID
        :return:
        '''
        params = {
            'id': im_id,
        }
        # 内置update方法加入上面的base_params参数
        params.update(self.base_params)
        r = requests.post(
            'http://upload.chaojiying.net/Upload/ReportError.php',
            data=params,
            headers=self.headers
        )
        return r.json()
