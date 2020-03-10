

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


# 2 常见反爬虫措施
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