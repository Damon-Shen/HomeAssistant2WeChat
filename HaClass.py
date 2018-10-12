#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
import os,re
import requests


class HomeAssistantHttpClient():

    def __init__(self,ha_url):
        self._ha_url = ha_url
        self.access_token = ""
        self.refresh_token = ""
        self.socure_url = ""

    def getToken(self,url):
        
        match_obj = re.findall(r'code=(\w+)', url, re.M|re.I)
        res = ''
        if match_obj:
            data = "grant_type=authorization_code&code=" + match_obj[0] + "&client_id=" + url.split('?')[0]
            
            res = requests.post(url=self._ha_url + "/auth/token",data=data,headers={'Content-Type':'application/x-www-form-urlencoded'})
            res = json.loads(res.text)
            self.access_token = res['access_token']
            self.refresh_token = res['refresh_token']
            self.socure_url = url.split('?')[0]
        else:
            res = "<script>window.location.href='" + self._ha_url + "/auth/authorize?client_id=" + url +"&redirect_uri=" + url +"?auth_callback=1'" + ";</script>"
            
        return res

    def __refresh_token(self):
        data = "grant_type=refresh_token&refresh_token=" + self.refresh_token + "&client_id=" + self.socure_url
        res = requests.post(url=self._ha_url + "/auth/token",data=data,headers={'Content-Type':'application/x-www-form-urlencoded'})
        res = json.loads(res.text)
        self.access_token = res['access_token']
    
    def LightControl(self,entity_id,mode):

        t = self.__testAuth()
        if (t == '401: Unauthorized'):
            self.__refresh_token()
        if (t == 'No Token'):
            return '没有获取Token'
        
        api_url = self._ha_url + "/api/states/" + entity_id
        header = {'Authorization': "Bearer " + self.access_token}
        response = requests.get(url = api_url,data = "",headers=header)

        if (response.status_code == 200):
            
            if (mode == 1):
                if (json.loads(response.text)['state'] == 'on'):
                    return 0
                else:
                    api_url =  self._ha_url + "/api/services/light/turn_on"
                    Postdata = {"entity_id": entity_id}
                    header = {'Content-Type':'application/json','Authorization': "Bearer " + self.access_token}
                    response = requests.post(url = api_url,data = json.dumps(Postdata),headers=header)
                    
                    if (response.status_code == 200):
                        return 'sucess'
                    else:
                        return response.text
                
            elif (mode == 0):
                if (json.loads(response.text)['state'] == 'off'):
                    return 0
                else:
                    api_url =  self._ha_url + "/api/services/light/turn_off"
                    Postdata = {"entity_id": entity_id}
                    header = {'Content-Type':'application/json','Authorization': "Bearer " + self.access_token}
                    response = requests.post(url = api_url,data = json.dumps(Postdata),headers=header)
                    if (response.status_code == 200):
                        return 'sucess'
                    else:
                        return response.text

    def SwitchControl(self,entity_id,mode):

        t = self.__testAuth()
        if (t == '401: Unauthorized'):
            self.__refresh_token()
        if (t == 'No Token'):
            return '没有获取Token'
        
        api_url = self._ha_url + "/api/states/" + entity_id
        header = {'Authorization': "Bearer " + self.access_token}
        response = requests.get(url = api_url,data = "",headers=header)
        if (response.status_code == 200):
            if (mode == 1):
                if (json.loads(response.text)['state'] == 'on'):
                    return 0
                else:
                    api_url =  self._ha_url + "/api/services/switch/turn_on"
                    Postdata = {"entity_id": entity_id}
                    header = {'Content-Type':'application/json','Authorization': "Bearer " + self.access_token}
                    response = requests.post(url = api_url,data = json.dumps(Postdata),headers=header)
                    if (response.status_code == 200):
                        return 'sucess'
                    else:
                        return response.text
                
            elif (mode == 0):
                if (json.loads(response.text)['state'] == 'off'):
                   return 0
                else:
                    api_url =  self._ha_url + "/api/services/switch/turn_off"
                    Postdata = {"entity_id": entity_id}
                    header = {'Content-Type':'application/json','Authorization': "Bearer " + self.access_token}
                    response = requests.post(url = api_url,data = json.dumps(Postdata),headers=header)
                    if (response.status_code == 200):
                        return 'sucess'
                    else:
                        return response.text

    def SensorState(self,entity_id):
        t = self.__testAuth()
        if (t == '401: Unauthorized'):
            self.__refresh_token()
        if (t == 'No Token'):
            return '没有获取Token'
        
        api_url = self._ha_url + "/api/states/" + entity_id
        header = {'Authorization': "Bearer " + self.access_token}
        response = requests.get(url = api_url,data = "",headers=header)
        if (response.status_code == 200):
            return json.loads(response.text)['state'] + json.loads(response.text)['attributes']['unit_of_measurement']
        else:
            return response.text
    
    def __testAuth(self):

        if (self.access_token == ''):
            return 'No Token'
        url = self._ha_url + "/api"
        headers = {
            'Authorization': "Bearer " + self.access_token,
        }
        response = requests.request('GET', url, headers=headers)

        return response.text