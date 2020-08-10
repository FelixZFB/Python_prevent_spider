# 6 App 反爬虫
- Web 站点有多种渲染和反爬方式，渲染分为服务端渲染和客户端渲染；反爬也是多种多样，
- 如请求头验证、WebDriver 限制、验证码、字体反爬、封禁 IP、账号验证等等，
- 综合来看 Web 端的反爬虫方案也是多种多样

- App 的情况略有不同，一般来说，App 的数据通信大都需要依赖独立的服务器，
- 比如请求某个 HTTP 接口来获取数据或做登录校验等。这种通信其实就类似 Web 中的 Ajax，
- 客户端向服务器发起 HTTP 请求，获取到数据之后再做一些处理，数据的格式大多也是 JSON、XML 等，
- 基本不会有 HTML 代码这样的数据，所以说，对于 App 来说，其核心就在于找到这些数据请求到底是怎样的，
- 比如某次 HTTP POST 请求的 URL、Headers、Data 等等，知道了这些，
- 我们就能用程序模拟这个请求过程，从而就能完成爬虫了。


## 6.1 App 抓包
- App 到底在运行过程中发起了什么请求呢？最有效且常见的方式就是抓包了，抓包工具也非常多，
- 比如 Fiddler、Charles、mitmproxy、anyproxy 等等，我们用这些工具抓到 HTTP 请求包，
- 就能看到这个请求的 Method、Headers、Data 等内容了，知道了之后再用程序模拟出来就行了。
- 抓包是利用第三方作为代理，实现监听网络传输与收发数据的行为

- App 的数据也是非常宝贵的，所以一些 App 也添加了各种反爬措施，比如：
    - 这个 App 的请求根本抓不到包，原因可能是 App 本身设置了不走系统代理。
    - 对一些 HTTPS 的请求，抓包失败，原因可能是系统或 App 本身设置了 SSL Pining，对 HTTPS 证书进行了校验，代理软件证书校验不通过，拒绝连接。
    - 某些包即使抓到了，也发现了其中带了加密参数，比如 sign、token 等等，难以直接用程序模拟。
    - 为了破解一些加密参数可能需要对 App 进行逆向，逆向后发现是混淆后的代码，难以分析逻辑。
    - 一些 App 为了防止逆向，本身进行了加固，需要对 App 进行脱壳处理才能进行后续操作。
    - 一些 App 将核心代码进行编译，形成 so 库，因此可能需要对 so 库进行逆向才能了解其逻辑。
    - 一些 App 和其服务器对以上所有的流程进行了风控处理，如果发现有疑似逆向或破解或访问频率等问题，返回一些假数据或拒绝服务，导致爬虫难以进行。

### 6.1.1 App 抓包
- 抓包
    - 对于多数情况来说，一台 Android 7.0 版本以下的手机，抓一些普通的 App 的请求包还是很容易做到的。
    - 抓包的工具有很多，常见的如 Charles、Fiddler、mitmproxy、Wireshark等。
    - 注意抓包软件和要抓包的电脑或者手机要处于同一个网络

- 抓包过程
    - 抓包的时候在 PC 端运行抓包软件，抓包软件会开启一个 HTTP 代理服务器，
    - 然后手机和 PC 连在同一个局域网内，设置好抓包软件代理的 IP 和端口，
    - 另外 PC 和手机都安装抓包软件的证书并设置信任。
    - 这样在手机上再打开 App 就能看到 App 在运行过程中发起的请求了。

- 抓包数据
    - 抓包完成之后在抓包软件中定位到具体数据包，查看其详情，
    - 了解其请求 Method、URL、Headers、Data，如果这些没有什么加密参数的话，
    - 我们用 Python 重写一遍就好了。
    - 当然如果遇到抓不到包或者有加密参数的情形，无法直接重写，那就要用到后面介绍的方法了。

### 6.1.2 App 代理抓不到包
- 抓不到包
    - 一些 App 在内部实现的时候对代理加了一些校验，
    - 如绕过系统代理直接连接或者检测到了使用了代理，直接拒绝连接。
    - 这种情形往往是手机的 HTTP 客户端对系统的网络环境做了一些判断，
    - 并修改了一些 HTTP 请求方式，使得数据不走代理，这样抓包软件就没法直接抓包了。
    - 另外对于一些非 HTTP 请求的协议，利用常规的抓包软件也可能抓不到包。这里提供一些解决方案。

- 强制全局代理
    - 虽然有些数据包不走代理，但其下层还是基于 TCP 协议的，所以可以将 TCP 数据包重定向到代理服务器。
    - 比如软件 ProxyDroid 就可以实现这样的操作，这样我们就能抓到数据包了。
    - ProxyDroid：https://github.com/madeye/proxydroid

- 手机代理
    - 如果不通过 PC 上的抓包软件设置代理，还可以直接在手机上设置抓包软件，
    - 这种方式是通过 VPN 的方式将网络包转发给手机本地的代理服务器，
    - 代理服务器将数据发送给服务端，获取数据之后再返回即可。
    - 使用了 VPN 的方式，我们就可以截获到对应的数据包了，
    - 一些工具包括 HttpCanary、Packet Capture、NetKeeper 等。
        - HttpCanary：https://play.google.com/store/apps/details?id=com.guoshi.httpcanary
        - Packet Capture：https://play.google.com/store/apps/details?id=app.greyshirts.sslcapture
        - NetKeeper：https://play.google.com/store/apps/details?id=com.minhui.networkcapture.pro
        - 以上应用链接来源于 Google Play，也可以在国内应用商店搜索或直接下载 apk 安装。

- 特殊协议抓包
    - 可以考虑使用 Wireshark、Tcpdump 在更底层的协议上抓包，比如抓取 TCP、UDP 数据包等等。
    - 使用的时候建议直接 PC 上开热点，然后直接抓取 PC 无线网卡的数据包，
    - 这样 App 不管有没有做系统代理校验或者使用了非 HTTP 协议，都能抓到数据包了。


### 6.1.3 SSL Pining
- SSL Pining，就是证书绑定，这个只针对 HTTPS 请求。
- SSL Pining 发生在下面的一些情况：
    - 对于 Android 7.0 以上的手机，系统做了改动，HTTPS 请求只信任系统级别证书，
    - 这会导致系统安全性增加，但是由于抓包软件的证书并不是系统级别证书，就不受信任了，那就没法抓包了。
    - 一些 App 里面专门写了逻辑对 SSL Pining 做了处理，对 HTTPS 证书做了校验，
    - 如果发现是不在信任范围之内的，那就拒绝连接。对于这些操作，我们通常有两种思路来解决：

- SSL Pining 解决方法    
    - 让系统信任我们的 HTTPS 证书；
    - 绕开 HTTPS 证书的校验过程。
    - 对于这两种思路，有以下一些绕过 SSL Pining 的解决方案。

- 方案1：修改 App 的配置
    - 如果是 App 的开发者或者把 apk 逆向出来了，那么可以直接通过修改 AndroidManifest.xml 文件，
    - 在 apk 里面添加证书的信任规则即可，
    - 详情可以参考 https://crifan.github.io/app_capture_package_tool_charles/website/how_capture_app/complex_https/https_ssl_pinning/，
    - 这种思路属于第一种信任证书的解决方案。

- 方案2：将证书设置为系统证书
    - 当然也可以将证书直接设置为系统证书，只需要将抓包软件的证书设置为系统区域即可。
    - 但这个前提是手机必须要 ROOT，而且需要计算证书 Hash Code 并对证书进行重命名，
    - 具体可以参考 https://crifan.github.io/app_capture_package_tool_charles/website/how_capture_app/complex_https/https_ssl_pinning，
    - 这种思路也是第一种信任证书的解决方案。






## 6.2 APK反编译


## 6.3 代码混淆