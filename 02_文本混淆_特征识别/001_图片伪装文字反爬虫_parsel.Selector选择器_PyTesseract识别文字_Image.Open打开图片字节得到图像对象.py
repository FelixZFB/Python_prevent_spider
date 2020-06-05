# -*- coding:utf-8 -*-
# project_xxx\venv\Scripts python

'''
Author: Felix
WeiXin: AXiaShuBai
Email: xiashubai@gmail.com
Blog: https://blog.csdn.net/u011318077
Date: 2020/3/12 15:17
Desc:
'''
import io
import requests
from urllib.parse import urljoin
from parsel import Selector
from PIL import Image
import pytesseract

url = 'http://www.porters.vip/confusion/recruit.html'
res = requests.get(url)
html = Selector(res.text)
# 从图片中提取图片链接的属性
# 使用xpath选择器提取
# image_url = html.xpath('//img[@class="pn"]/@src').extract_first()
# 使用css选择器提取
image_url = html.css('.pn::attr("src")').extract_first()
# 拼接完整的url
image_url = urljoin(url, image_url)
# 请求获取图片的字节数据
image_bytes = requests.get(image_url).content
# 打开图片的字节数据，得到图片对象
image_object = Image.open(io.BytesIO(image_bytes))
# 使用PyTesseract识别图片中的文字为字符串
text = pytesseract.image_to_string(image_object)
print(text)