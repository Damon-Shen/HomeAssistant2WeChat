#!/usr/bin/env python
# -*- coding: utf8 -*-


import HaClass
import config
import re,json
import requests
from werobot import WeRoBot

robot = WeRoBot(token=config.wx_token)

t1 = HaClass.HomeAssistantHttpClient(config.ha_url)


@robot.text
def response(message):
    
    match_states = re.findall(config.check_word_list, message.content, re.M|re.I)
    match_open = re.findall(config.open_word_list, message.content, re.M|re.I)
    match_close = re.findall(config.close_word_list, message.content, re.M|re.I)
   
    if len(match_states)==1:
        for k,v in config.sensor_dic.items():
            sensor = list(filter(None, match_states[0]))
            if (k == sensor[0]):
                t3 = t1.SensorState(config.sensor_dic[k])
                if (t3 != -1):
                    return '当前' + k + "为" + t3
                else:
                    return t3
 
    elif len(match_open)==1:
        for k,v in config.light_control_dic.items():
            light = list(filter(None, match_open[0]))
            switch = list(filter(None, match_open[0]))
            for k2,v2 in config.switch_control_dic.items():
                if (k == light[0]):
                    t3 = t1.LightControl(config.light_control_dic[k],1)
                    if (t3 == 0):
                        return '当前' + k + "为打开状态"
                    elif (t3 == 'sucess'):
                        return k + "已经打开"
                    else:
                        return t3
                if (k2 == switch[0]):
                    t3 = t1.SwitchControl(config.switch_control_dic[k2],1)
                    if (t3 == 0):
                        return '当前' + k2 + "为打开状态"
                    elif (t3 == 'sucess'):
                        return k2 + "已经打开"
                    else:
                        return t3
            

    elif len(match_close)==1:
        for k,v in config.light_control_dic.items():
            light = list(filter(None, match_close[0]))
            switch = list(filter(None, match_close[0]))
            for k2,v2 in config.switch_control_dic.items():
                if (k == light[0]):
                    t3 = t1.LightControl(config.light_control_dic[k],0)
                    if (t3 == 0):
                        return '当前' + k + "为关闭状态"
                    elif (t3 == 'sucess'):
                        return k + "已经关闭"
                    else:
                        return t3
                if (k2 == switch[0]):
                    t3 = t1.SwitchControl(config.switch_control_dic[k2],0)
                    if (t3 == 0):
                        return '当前' + k2 + "为关闭状态"
                    elif (t3 == 'sucess'):
                        return k2 + "已经关闭"
                    else:
                        return t3

@robot.error_page
def make_error_page(url):
    res = t1.getToken(url=url)
    if isinstance(res,dict):
        if 'access_token' in res:
            return 'Token已获取'
        else:
            return '无法获取Token'
    else:
        return res

# 让服务器监听在 0.0.0.0:8888
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 8888
# robot.config['SERVER'] = 'tornado'
robot.run()