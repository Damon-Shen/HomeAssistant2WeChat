#!/usr/bin/env python
# -*- coding: utf8 -*-

ha_api_passwd = 'sky5201314'                     #homeassistant api密码
ha_url = 'https://home.8023.online:9123'         #homeassistant 地址
wx_token = 'MyToken'

open_word_list = r'打开(\w+)*|启动(\w+)*'
close_word_list = r'关闭(\w+)*|停止(\w+)*'
check_word_list = r'查询(\w+)*|现在(\w+)*'



#定义灯具dic
light_control_dic = {
    "卧室灯":"light.gateway_light_34ce008db6e0",
    "客厅灯":""
}

#定义插座dic
switch_control_dic = {
    "热水器":"switch.bathroom",
    "风扇":"switch.fan"
}

#定义温度传感器dic
temperature_sensor_dic = {
    "客厅温度":"sensor.temperature",
    "卧室温度":"sensor.temperature_158d0002374f06"
}

#定义湿度传感器dic
humidity_sensor_dic = {
    "客厅湿度":"sensor.humidity",
    "卧室湿度":"sensor.humidity_158d0002374f06"
}

#定义气压传感器dic
pressure_sensor_dic = {
    "客厅气压":"",
    "卧室气压":"sensor.pressure_158d0002374f06"
}

#定义光感传感器dic
light_sensor_dic = {
    "客厅亮度":"sensor.lux",
    "卧室亮度":"sensor.illumination_mi"
}





