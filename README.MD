

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
        
