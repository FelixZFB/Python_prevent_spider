# Python3实现有道在线翻译案例
# 有道在线翻译http://fanyi.youdao.com/

import json
from urllib import request, parse

if __name__ == '__main__':

    key = input("请输入需要翻译的文字(输入完成后请按Enter): ")

    # 打开有道在线翻译，输入girl，检查，找到headers,复制里面的网址
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    # 将网页中的Form Data中的所有数据复制出来
    # 通过调试发现，只需要其中的i对应要翻译的内容和doctype对应的数据格式
    formdata = {
        'i': key,
        'doctype': 'json',
    }

    # formdata中的数据需要转换为bytes格式
    data = parse.urlencode(formdata).encode()

    # 将网页中的请求头Request Headers中的数据复制出来,只需要一个用户代理即可
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71',
    }

    # 请求网页
    req = request.Request(url=url, data=data, headers=headers)

    # 返回网页
    res = request.urlopen(req)

    # 下载导出数据
    result = json.loads(res.read())

    # 打印出翻译后的结果
    print("\n翻译结果: " + result["translateResult"][0][0]["tgt"])





