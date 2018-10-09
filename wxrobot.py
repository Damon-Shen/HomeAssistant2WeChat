#!/usr/bin/env python
# -*- coding: utf8 -*-

import werobot
import HaClass
import config
import re

robot = werobot.WeRoBot(token=config.wx_token)
t1 = HaClass.HomeAssistantHttpClient(config.ha_url,config.ha_api_passwd)


@robot.text
def response(message):
    
    match_states = re.findall(config.check_word_list, message.content, re.M|re.I)
    match_open = re.findall(config.open_word_list, message.content, re.M|re.I)
    match_close = re.findall(config.close_word_list, message.content, re.M|re.I)
   
    if len(match_states)==1:
        for k,v in config.temperature_sensor_dic.items():
            sensor = list(filter(None, match_states[0]))
            if (k == sensor[0]):
                t3 = t1.SensorState(config.temperature_sensor_dic[k])
                if (t3 != -1):
                    return '当前' + k + "为" + t3
                else:
                    return '无法获取设备状态'
 
    elif len(match_open)==1:
        for k,v in config.light_control_dic.items():
            light = list(filter(None, match_open[0]))
            switch = list(filter(None, match_open[0]))
            for k2,v2 in config.switch_control_dic.items():
                if (k == light[0]):
                    t3 = t1.LightControl(config.light_control_dic[k],1)
                    if (t3 == 0):
                        return '当前' + k + "为" + t3
                    elif (t3 == 'sucess'):
                        return k + "已经打开"
                    else:
                        return '无法获取设备状态'
                if (k2 == switch[0]):
                    t3 = t1.SwitchControl(config.switch_control_dic[k2],1)
                    if (t3 == 0):
                        return '当前' + k2 + "为" + t3
                    elif (t3 == 'sucess'):
                        return k2 + "已经打开"
                    else:
                        return '无法获取设备状态'
            

    elif len(match_close)==1:
        for k,v in config.light_control_dic.items():
            light = list(filter(None, match_close[0]))
            switch = list(filter(None, match_close[0]))
            for k2,v2 in config.switch_control_dic.items():
                if (k == light[0]):
                    t3 = t1.LightControl(config.light_control_dic[k],0)
                    if (t3 == 0):
                        return '当前' + k + "为开启状态"
                    elif (t3 == 'sucess'):
                        return k + "已经关闭"
                    else:
                        return '无法获取设备状态'
                if (k2 == switch[0]):
                    t3 = t1.SwitchControl(config.switch_control_dic[k2],0)
                    if (t3 == 0):
                        return '当前' + k2 + "为关闭状态"
                    elif (t3 == 'sucess'):
                        return k2 + "已经关闭"
                    else:
                        return '无法获取设备状态'
    else:
        return '无此关键词'
   
        
        
       


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8888
robot.run()