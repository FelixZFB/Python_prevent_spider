
# 0 前言
## 0.1 反爬虫按设计目的分类
- 限制手段
    - 请求限制、拒绝响应、客户端身份验证、文本混淆、动态渲染等手段
- 主动型反爬虫
    - 开发者有意识的使用技术手段区分正常用户和爬虫，并限制爬虫对网站的访问行为。
    - 比如验证请求头信息、限制访问的频率、使用验证码等
- 被动型反爬虫
    - 为了提升用户体验和节省资源，使用了一些技术间接提高了爬虫访问难度的行为
    - 比如数据分段加载(js动态加载数据)、点击切换标签页(切换时候请求加载数据)、鼠标悬停预览数据(鼠标悬停动作加载数据)
    

## 0.2 反爬虫按特点分类
- 信息校验型反爬虫：网络请求阶段，预防为主要目的，尽可能的拒绝爬虫的请求
- 动态渲染型反爬虫：文本获取和数据提取阶段，保护数据为主要目的，尽可能避免爬虫获取重要数据
- 文本混淆反爬虫：文本获取和数据提取阶段，保护数据为主要目的，尽可能避免爬虫获取重要数据
- 特征识别反爬虫：预防为主要目的，直指爬虫出现的源头
- APP反爬虫：
- 验证码反爬虫：

## 反爬虫



# 1 环境配置
## 1.1 Docker容器
- Docker容器可以和虚拟机一样实现资源和系统环境的隔离
- Docker是一个用Go语言编写的开源的应用容器引擎
    - 特点：轻量、便捷、低开销
    - 用途：允许开发者将应用和对应的运行环境包装到一个可移植的容器中，并
    发布到任何装有Docker的机器上
- Docker与VM虚拟机的区别：
    - VM(VMware)在宿主机器、宿主机器操作系统的基础上创建虚拟层、虚拟化的操作系统、虚拟化的仓库，然后再安装应用；
    - Container(Docker容器)，在宿主机器、宿主机器操作系统上创建Docker引擎，在引擎的基础上再安装应用。
    - Docker在宿主机器的操作系统上创建Docker引擎，直接在宿主主机的操作系统上调用硬件资源，而不是虚拟化操作系统和硬件资源，所以操作速度快。
- Docker安装参考博文：
[Ubuntu18.04 安装Docker（安装常见报错及Docker常用命令）](https://blog.csdn.net/u011318077/article/details/104733149)

## 1.2 yum命令安装
- yum（ Yellow dog Updater, Modified）是一个在Fedora和RedHat以及SUSE中的Shell前端软件包管理器。
- yum 语法,使用和pip命令类似
    - yum [options] [command] [package ...]
    - options：可选，选项包括-h（帮助），-y（当安装过程提示选择全部为"yes"），-q（不显示安装的过程）等等。
    - command：要进行的操作。
    - package操作的对象。
    - sudo yum install pam-devel   安装包
    - sudo yum remove pam-devel    卸载包
- ubuntu18.04安装yum命令：sudo apt-get install yum

## 1.3 nginx服务安装
- Nginx是一款轻量级的Web 服务器/反向代理服务器及电子邮件（IMAP/POP3）代理服务器，在BSD-like 协议下发行。
- 特点是占有内存少，并发能力强，事实上nginx的并发能力在同类型的网页服务器中表现较好

- nginx安装：
    - sudo apt-get install nginx      安装命令
    - sudo /etc/init.d/nginx status   查看nginx运行状态
    - sudo /etc/init.d/nginx start    启动nginx
    - sudo /etc/init.d/nginx restart  重启nginx
    - sudo nginx -s reload            不重启下重载配置文件，一般修改配置文件后执行改命令
    - sudo find / -name nginx.conf    查看当前使用的配置文件

- 安装完成后：访问 http://localhost  显示Welcome to nginx!

- nginx文件说明：
    - 程序文件在 /usr/sbin/nginx
    - 日志文件 /var/log/nginx
    - 一些相关配置文件在 /etc/nginx/*下
    - 存放静态文件 /usr/share/nginx 

- [Ubuntu 16.04安装Nginx以及相关配置](https://blog.csdn.net/javahighness/article/details/80500437?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)


# 2 信息验证型反爬虫
## 2.1 User-Agent反爬虫
- User-Agent是用户身份识别的重要信息，User-Agent中包含用户浏览器、浏览器引擎、操作系统等信息
- python的requests库请求时候，服务器读取到的User-Agent信息就是 python-requests/2.21.0
- User-Agent反爬虫：
    - nginx中加入User-Agent检测，将python，Java，PHP等一些关键词都加入到黑名单中
    - 检测时候，发现含有这些关键词，就认定为是爬虫程序
- 除了User-Agent头部信息，常用的还有Host,Referer头部信息
    - 1. Host 描述请求将被发送的目的地，只含域名和端口号；
    - 2. Origin 请求是从哪里发起的，包括域名和端口号，这个参数一般存在于CORS跨域请求中，
        可以看到response有对应的header: Access-Control-Allow-Origin
    - 3. Referer 告知服务器请求的原始资源的URI,其用于所有类型的请求，包括：协议+域名+查询参数


## 2.2 Cookies反爬虫
- 服务器端，一般是Nginx中加入检测请求头信息中是否有http_cookie信息,然后返回不同的结果。
- 浏览器正常请求网页，服务器返回的cookie会自动保存在本地，下次访问时候会自动携带
- 没有携带cookie访问，返回结果都是重定向，一般都是重定向30x,一般都是定位到首页或者登陆页面

## 2.3 签名验证反爬虫
- JavaScript异步动态请求类型一般都是xhr(ajax封装对象)，可以在请求里面查找类型为xhr的请求，请求源一般都是js文件
- 请求正文内容里面有特征值是32位（一般是MD5加密后字段），一般可以大胆猜测就是签名验证反爬虫，
- 加密内容都是使用JavaScript里面的函数生成的，通过进js文件搜索关键字，就可以找到加密字段的生成方式

- 案例1：
- 访问一下网址，然后点击查看详情
    - http://www.porters.vip/verify/sign/
    - 上述网址，点击查看详情，查看network
    - 下面网址就是动态加密生成的，直接复制去请求是无效的，网址有多个参数还有时间戳，直接浏览器再次去请求就是无效的
    - http://www.porters.vip/verify/sign/fet?actions=31288&tim=1583827827&randstr=JUBMB&sign=1f46e27e48caacc155fbf9afde6bbbc0
    - 动态加密请求，就是需要破解动态网址是如何生成的
    - 点击查看详情，network里面有一个fet.....开头的网址请求，类型是xhr(ajax封装的对象)

- 查看网址，点击查看详情位置，参考图片005，发现onclick绑定一个fetch()函数
    - 表明点击后执行该函数，函数都是放在js代码里面，head里面发现引入了两个自定义的js文件
    - Chrome检查，查看，右键在js文件上，open in new tab
    - 查看fetch()函数具体内容，函数访问一个动态生成的网址，网页内容插入替换原始网页id="content"标签的内容
    - 然后我们在python中实现该真实网址的生成方式

- 案例2：
- 有道翻译加密分析：
    - 打开有道翻译，输入中国，network里面出现一个xhr类型的post请求，请求源Initiator是一个js文件
    - post请求，Request URL: http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
    - 请求体的formdata里面有很多参数，i就是要翻译的字符串
    - 加密的参数进请求源js文件里面搜索，可以找到参数的生成方式
    - 具体参考006图片
    - 实际有道翻译加密只需要保留formdata中的i和doctype就可以获取翻译后的json数据，直接忽略加密内容
    - 参考006案例
    
    
## 2.4 js动态请求补充：
- 网页源码中（Name，Status，Type，Initiator，Size，Time，Waterfall）的含义
    - 第一列 Name ：请求的名称，一般会将URL 最后一部分内容当作名称
    - 第二列 Status ：响应的状态码，显示为 200 代表响应是正常的 通过状态码，我们可以判断发送了请求之后是否得到了正常的响应 。
    - 第三列 Type： 请求的文档类型 。这里为 document ，代表我们这次请求的是 HTML 文档， 内容就是一些 HTML 代码。
    - 第四列 Initiator： 请求源。 用来标记请求是由哪个对象或进程发起的
    - 第五列 Size : 从服务器下载的文件和请求的资源大小。 如果是从缓存中取得的资源，则该列 会显示from cache。
    - 第六列 Time : 发起请求到获取响应所用的总时间
    - 第七列 Waterfall：网络请求的可视化瀑布流

- 动态ajax请求一般是xhr类型
    - xhr：XMLHttpRequest在后台与服务器交换数据，这意味着可以在不加载整个网页的情况下，对网页某部分的内容进行更新。
    是Ajax的一种用法，而Ajax并不是一门语言，只是一种不需要加载整个网页，只是更新局部内容的技术。

    - 案例：
    - 比较常见的就是网页内容繁多，我们仅仅看评论时，无需整个页面都加载，
    - 那么就可以采用这种方式来实现，只需要在翻页时，局部加载评论的内容即可。

- js(ajax)动态请求
    - 1、在使用Chrome或者firebug抓取类似网页的内容时，只需要找到xhr类型的url地址，Initiator请求源一般是一个js文件
    - 2、在浏览器地址栏中打开即可看到对应的内容。
    - 3、一般情况为json格式，
    - 4、再利用python等语言抓取json中的需要的内容即可
    

# 3 动态渲染反爬虫  
## 3.1 Selenium工具
- 工具1：Selenium + Chrome + 驱动器 三件套抓取动态渲染网页
    - 缺点：执行效率低，占用系统资源大，不能异步请求

## 3.2 Puppeteer工具
- 工具2：Puppeteer(python中的库叫pyppeteer)
- 安装：
    - 安装命令：
        pip install pyppeteer
        python -m pip install pyppeteer
    - 从GIT安装最新版本：python -m pip install -U git+https://github.com/miyakogi/pyppeteer.git@dev
    
    - 推荐安装方式：
        - 第一步：需要先安装支持库 pip install tdqm
        - 第二步：pip install pyppeteer
        - 第三步：含有pyppeteer的代码运行时候，会自动下载chromium解压安装（Chrome的实验版）
- 参考案例008

## 3.3 Splash异步渲染服务
- Splash是一个异步的JavaScript的渲染服务，它带有HTTP API的轻量级Web服务器。
- 可视化界面地址：http://www.porters.vip:8050/      
- 上面地址输入网址，然后render me就可以获取网页的截图、资源加载数据、HTML原始文本
- 脚本里面也可以自己编写，但是使用的是Lua语言
- 参考009图片

- Splash服务也可以和Python语言结合使用
- 参考案例009

- 上面三种渲染工具对比：
    - Selenium套件通过驱动浏览器执行操作，本质上是模拟浏览器操作
    - Puppeteer实际上通过API控制Chromium或者Chrome浏览器
    - Splash基于开源的浏览器引擎WebKit
    

# 4 文本混淆反爬虫
## 4.1 图片伪装为文字反爬虫
- 有些文字内容实际是图片伪装的
- 提取图片的内容(图片请求响应结果res.content就是图片的字节数据，可以直接write为图片对象，也可以打开为图片对象，看案例)
- 图片对象使用光学字符识别技术(pytesseract库)从图片中提取文字
- PyTesseract缺点：只能识别出一些清晰工整的图像中的文字，扭曲的文字或者有其它颜色图片干扰信息时候识别不准确
- 参考案例001(02文件夹中)

## 4.2 CSS偏移反爬虫
- 一般用于数字显示，源码中有很多数字，用于混淆
- 网页中显示的出来的内容的位置是固定的，源码中的数字进行偏移覆盖才是最终显示出来的数字
- 去哪儿网的航班票价就是进行CSS偏移处理过的
- 前面有数字120  下面有数字002
- 002通过不同的左右偏移位置覆盖在120的数字上才是最终显示结果
- 参考图片002

## 4.3 SVG图形映射反爬虫
- SVG是一种二维矢量图形格式，放大缩小清晰度保持不变
- SVG映射反爬虫：前端或者后端里面将文字或者数字映射为对应SVG图形文件
网页源码中显示的是SVG图形文件，并没有实际的文字或者数字内容
- 最常用于团购网站商家电话的替换
- 映射替换有两种方式：
    - 方式1：一个SVG图片代表一个数字或者文字。要显示内容的地方使用SVG图片替代，一般是设置class样式，然后设置背景图片，用SVG图片插到盒子中
    - 方式2：将所有的数字或者文字都放在一张SVG图片上，然后设置为背景图片，然后通过偏移图片的位置显示内容
    - 方式3：将所有的数字或者文字都放在一张SVG图片上，然后设置为背景图片，图片位置不同，SVG图片里面的的数字是可以通过改变xy轴坐标显示的位置的
    - 具体参考图书的P181页，关键是找到映射的规律
    
## 4.4 自定义网页字体(常用woff格式字体)反爬虫
- 自定义的字体格式：woff ttf eot otf
- 文中的数字使用自定义字体样式进行替代，查看元素数字都是显示的方框或者其它特殊符号
- 查看元素里面可以数字都有一个class样式，查看该class样式具体内容，只用一个font-family，对应的值就是自定义的字体样式
- 查看源码，数字是一些特殊编码，特殊编码就是字体文件里面定义的数字对应的编码
- woff等字体文件请求的网址，可以下载字体文件到本地，然后使用
- 百度在线字体编辑打开查看：http://fontstore.baidu.com/static/editor/index.html
- 参考003图片

- WOFF字体文件研究
    - WOFF(Web Open Font Format, web开放字体样式)是一种网页采用的字体格式标准
    - 本质上WOFF是基于SFNT字体，具有TrueType字体的结构，TrueType字体由网格上一系列的点进行描述，点是字体的最小单位
    - WOFF文件等字体文件可以使用python中的第三方fonttools转换为XML文件，便于观察里面的具体数据
    - pip install fonttools
    - 参考案例004
    - 打开XML文件，下面内容就是描述数字6的字形文件
        - TTGlyph里面有字形的名称、x和y轴坐标数据（可理解为字形的宽和高）
        - contour里面只字形的轮廓信息，即多个点的坐标位置，就是这些点连接在一起构成一个字形
    - 注意：相同的字形的宽高或者轮廓点可能会不一样，但是它们描述的会是一个字形
        因此，只有起止坐标和点坐标数据完全一样的字形，我们才能肯定它们是相同的字符
```
<TTGlyph name="uniE339" xMin="0" yMin="-12" xMax="510" yMax="719">
      <contour>
        <pt x="410" y="534" on="1"/>
        <pt x="398" y="586" on="0"/>
        <pt x="377" y="609" on="1"/>
        <pt x="341" y="646" on="0"/>
        <pt x="289" y="646" on="1"/>
        <pt x="247" y="646" on="0"/>
        <pt x="215" y="623" on="1"/>
        <pt x="173" y="592" on="0"/>
        <pt x="150" y="535" on="1"/>
        <pt x="138" y="506" on="0"/>
        <pt x="125" y="423" on="0"/>
        <pt x="125" y="369" on="1"/>
        <pt x="157" y="418" on="0"/>
        <pt x="248" y="464" on="0"/>
        <pt x="299" y="464" on="1"/>
        <pt x="386" y="464" on="0"/>
        <pt x="510" y="334" on="0"/>
        <pt x="510" y="232" on="1"/>
        <pt x="510" y="165" on="0"/>
        <pt x="452" y="49" on="0"/>
        <pt x="352" y="-12" on="0"/>
        <pt x="286" y="-12" on="1"/>
        <pt x="176" y="-12" on="0"/>
        <pt x="38" y="147" on="0"/>
        <pt x="38" y="335" on="1"/>
        <pt x="38" y="543" on="0"/>
        <pt x="114" y="637" on="1"/>
        <pt x="181" y="719" on="0"/>
        <pt x="294" y="719" on="1"/>
        <pt x="379" y="719" on="0"/>
        <pt x="433" y="671" on="1"/>
        <pt x="486" y="625" on="0"/>
        <pt x="498" y="541" on="1"/>
      </contour>
      <contour>
        <pt x="139" y="232" on="1"/>
        <pt x="139" y="188" on="0"/>
        <pt x="178" y="103" on="0"/>
        <pt x="247" y="60" on="0"/>
        <pt x="285" y="60" on="1"/>
        <pt x="339" y="60" on="0"/>
        <pt x="420" y="150" on="0"/>
        <pt x="420" y="227" on="1"/>
        <pt x="420" y="300" on="0"/>
        <pt x="341" y="387" on="0"/>
        <pt x="223" y="387" on="0"/>
        <pt x="139" y="301" on="0"/>
      </contour>
      <instructions/>
    </TTGlyph>
```

- 可以利用fonttools打开网页的字体文件进行分析
    - 找出每个字符映射到网页源码中的代码，实现WOFF字形文件的映射文件
    - 但是如果开发者经常更换字体文件或者使用多套woff字体文件随机切换(只需要引用路径随机更换即可，网页源码使用了字体样式，字符代码就会自动更换)
    - 会使爬取难度越来越大

## 4.5 文本混淆爬虫通用解决方法
- 光学字符识别OCR可以是识别图形中的文字，但是WOFF字体文件和SVG图形中文字太多或者干扰因素多的时候就无法识别
- 解决方法：
    - 使用Python连接Splash渲染工具，进行网页所需部分的截图
    - 拿到截图后保存到本地
    - 使用PyTesseract库识别指定的图片
    - 该方法缺点：PyTesseract是一个开源库，识别率较低
    - 解决方法: 使用第三方文字识别API
        - 腾讯云OCR识别（识别率高，但是要收费）
        - https://cloud.tencent.com/act/event/ocrdemo
    - 参考案例005及书中P202
      
      
# 5 特征识别爬虫
- HTML文档对象 DOM
    - HTML文档对象DOM(Document Object Model)  
    - HTML DOM对象是对HTML文档所有元素进行访问的入口，这个入口就是文档对象模型，简称DOM
    - DOM是W3C组织推荐的处理可扩展标志语言的标准编程接口
    - DOM以面向对象的方式描述文档模型，定义了表示和修改文档所需要的对象的名称、对象的行为、对象的属性以及和对象之间的关系
    - 在网页中，组织页面或者文档对象被放在一个树形的结构中，其中用来表示对象的标准模型就是DOM
    - HTML文档树形结构最顶层的对象就是document
    - DOM也可以理解为一个容器，EChats中绘图前都需要在网页中准备一个DOM容器对象

- 浏览器器对象 BOM
    - 浏览器对象模型BOM(Browser Object Model)
    - BOM对象是用来获取和操作浏览器的属性，主要对象有
        - window: 浏览器窗口，所有的JavaScript全局对象、函数和变量均自动成为该对象的成员
        - window.navigator：访问者浏览器的相关信息
        - window.location: 窗口当前显示的文档的web地址
        - window.screen: 访问者浏览器的屏幕信息

- 详细DOM和BOM对象属性和方法查看图书P66-P69

## 5.1 Webdriver识别反爬虫
- webdriver特征是可以修改的，不可靠
- 参考案例006

## 5.2 浏览器特征
- navigator.userAgent  浏览器器属性
- navigator.platform   用户计算机信息
- 参考截图007_浏览器特征
- 上面的浏览器特征也是和navigator.webdriver一样可以认为进行修改的，一样不可靠

## 5.3 爬虫特征
- IP地址访问频率限制：使用IP池，分布式爬虫(多台机器轮流访问)
- 用户凭证（cookie或者token）和浏览器指纹限制：
    - web框架自带访问频率限制：登陆用户每天访问1000次，未登录每天100次
    - web框架自带限速模块Throttling

- 用户凭证反爬虫：申请大量用户，访问时候随机携带cookie或token值，类似IP代理池
