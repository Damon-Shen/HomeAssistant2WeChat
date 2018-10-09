#!/usr/bin/env python
# -*- coding: utf8 -*-

import HaClass
import config

t1 = HaClass.HomeAssistantHttpClient(config.ha_url,config.ha_api_passwd)
t2 = t1.SwitchControl(config.switch_control_dic['风扇'],1)

# t3 = t1.SensorState(config.temperature_sensor_dic['客厅温度'])

print(t2)