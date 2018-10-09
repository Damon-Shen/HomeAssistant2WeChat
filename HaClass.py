#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
import os
import requests


class HomeAssistantHttpClient():
    
    def __init__(self,ha_url,ha_api_passwd):
        self._ha_api_passwd = ha_api_passwd
        self._ha_url = ha_url
    
    def LightControl(self,entity_id,mode):

        api_url = self._ha_url + "/api/states/" + entity_id + "?api_password=" + self._ha_api_passwd
        response = self.__request(url = api_url,data = '',flag = 1)
       
        if (response.status_code == 200):
            
            if (mode == 1):
                if (json.loads(response.text)['state'] == 'on'):
                    return 0
                else:
                    api_url =  self._ha_url + "/api/services/light/turn_on?api_password=" + self._ha_api_passwd
                    Postdata = {"entity_id": entity_id}
                    response = self.__request(api_url,Postdata,0)
                    if (response == 200):
                        return 'sucess'
                    else:
                        return -1
                
            elif (mode == 0):
                if (json.loads(response.text)['state'] == 'off'):
                    return 0
                else:
                    api_url =  self._ha_url + "/api/services/light/turn_off?api_password=" + self._ha_api_passwd
                    Postdata = {"entity_id": entity_id}
                    response = self.__request(api_url,Postdata,0)
                    if (response == 200):
                        return 'sucess'
                    else:
                        return -1
    def SwitchControl(self,entity_id,mode):

        api_url = self._ha_url + "/api/states/" + entity_id + "?api_password=" + self._ha_api_passwd
        response = self.__request(url = api_url,data = '',flag = 1)
        if (response.status_code == 200):
            if (mode == 1):
                if (json.loads(response.text)['state'] == 'on'):
                    return 0
                else:
                    api_url =  self._ha_url + "/api/services/switch/turn_on?api_password=" + self._ha_api_passwd
                    Postdata = {"entity_id": entity_id};
                    response = self.__request(api_url,Postdata,0);
                    if (response == 200):
                        return 'sucess'
                    else:
                        return -1
                
            elif (mode == 0):
                if (json.loads(response.text)['state'] == 'off'):
                   return 0
                else:
                    api_url =  self._ha_url + "/api/services/switch/turn_off?api_password=" + self._ha_api_passwd
                    Postdata = {"entity_id": entity_id}
                    response = self.__request(api_url,Postdata,0)
                    if (response == 200):
                        return 'sucess'
                    else:
                        return -1

    def SensorState(self,entity_id):
        api_url = self._ha_url + "/api/states/" + entity_id + "?api_password=" + self._ha_api_passwd
        response = self.__request(url = api_url,data = '',flag = 1);
        if (response.status_code == 200):
            return json.loads(response.text)['state'] + json.loads(response.text)['attributes']['unit_of_measurement']
        else:
            return -1

    def __request(self,url,data,flag):
        try:
            if (flag == 0):
                res = requests.post(url=url,data=json.dumps(data),headers={'Content-Type':'application/json'})
                return res.status_code
            else:
                res = requests.get(url=url)
                return res
        except Exception as e:
            return -1