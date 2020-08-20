# Appium 安装

# 安装步骤：
- 参考链接：https://cuiqingcai.com/5407.html
- 1 电脑端安装 Appium Desktop
    - Windows平台可以下载exe安装包appium-desktop-Setup-1.1.0.exe
    - Mac平台可以下载dmg安装包如appium-desktop-1.1.0.dmg
    - Linux平台可以选择下载源码，但是更推荐用Node.js安装方式
- 2 Android开发环境配置
    - 使用Android设备做App抓取的话，还需要下载和配置Android SDK，这里推荐直接安装Android Studio
    - 安装完成后打开软件，下载Android SDK
    - 配置一下环境变量，添加ANDROID_HOME为Android SDK所在路径，然后再添加SDK文件夹下的tools和platform-tools文件夹到PATH中。    
- 3 Python 驱动
    - pip3 install appium-python-client
    - 或 pip install appium-python-client
    - 或 pycharm 里面搜索 appium-python-client 安装

# 1 