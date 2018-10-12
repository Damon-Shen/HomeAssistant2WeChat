# HomeAssistant2WeChat
HomeAssistant使用微信公众号控制


Update 2018-10-12<br>
1、支持HomeAssistant Auth2认证方式，直接访问地址即可打开<br>
2、修正几个状态回馈错误的问题<br>

Python版本 3.6.6调试通过，个人精力有限，不做其他版本兼容
目前版本较为简陋，设备类型仅支持Light，Switch，Sensor，仅支持文字信息控制，关键词命令如下(关键词可在配置文件中修改，支持多个关键词匹配，需保留格式)<br>
```
打开+设备名称
关闭+设备名
查询+设备名
如：
打开风扇，开启风扇
查询卧室温度
```

公众号使用了WxRoBot框架：https://github.com/offu/WeRoBot


使用方法：</br>
1、安装WxRobot框架：</br>
`pip3 install wxrobot`</br>
2、申请微信公众号：</br>
未认证的公众号或个人号由于权限问题无法使用如自定义菜单接口（暂未添加此功能），可采用公众号测试平台进行自定义菜单调试，
公众号测试平台支持任意端口，本程序默认采用8888端口启用</br>
3、配置本地文件：</br>
随后在config.py文件中配置好HomeAssistant的地址，微信Token，设备信息，最后添加8888端口映射至外网</br>
4、启动服务：</br>
`python3 wxrbot.py`</br>
5、微信后台开启对接：</br>
在公众号测试平台中的接口配置信息中填入外网地址和token信息，即可在公众号测试平台使用文字信息控制


