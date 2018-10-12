#!/usr/bin/env python
# -*- coding: utf8 -*-

# import HaClass
# import config

# t1 = HaClass.HomeAssistantHttpClient(config.ha_url,config.ha_api_passwd)
# t2 = t1.SwitchControl(config.switch_control_dic['风扇'],1)

# t3 = t1.SensorState(config.temperature_sensor_dic['客厅温度'])

# t4 = t1.testAuth()

url = "http://127.0.0.1:8888/?auth_callback&code=33e5529d6e484a83985066bc9937d983"

print (url.split('?')[0][:-1])

# print(t4)