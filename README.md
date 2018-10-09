# HomeAssistant2WeChat
HomeAssistant使用微信公众号控制


HomeAssistant使用Legacy API Password方式登陆，暂未支持Auth2认证方式
Python版本 3.6.6调试通过，个人精力有限，不做其他版本兼容

公众号使用了WxRoBot框架：https://github.com/offu/WeRoBot


使用方法：</br>
1、安装WxRobot框架：</br>
`pip3 install wxrobot`</br>
2、申请微信公众号：</br>
未认证的公众号或个人号由于权限问题无法使用如自定义菜单接口（暂未添加此功能），可采用公众号测试平台进行自定义菜单调试，
公众号测试平台支持任意端口，本程序默认采用8888端口启用</br>
3、配置本地文件</br>
随后在config.py文件中配置好HomeAssistant的地址，Legacy API Password，微信Token，设备信息，最后添加8888端口映射至外网</br>
4、启动服务</br>
`python3 wxrbot.py`


