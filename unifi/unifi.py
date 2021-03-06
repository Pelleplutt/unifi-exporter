#!/usr/bin/env python3

import json
import logging
import os
import pprint
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning, SNIMissingWarning, InsecurePlatformWarning

from . import site

class UniFiException(Exception):
    apimsg = None

    def __init__(self, apimsg, s=None):
        m = s
        if m is None:
            m = apimsg
        super(UniFiException, self).__init__(m)

        self.apimsg = apimsg
class UniFiLoginRequiredException(UniFiException):
    pass

class UniFi(object):
    api_headers = {"Accept": "application/json", "Content-Type": "application/json"}
    def __init__(self, username, password, controller_addr=None, udm_addr=None):
        self.username = username
        self.password = password
        self.cookies = {}
        self.session = requests.Session()
        self.is_udm = False
        if controller_addr:
            self.is_udm = False
            self.addr = controller_addr
        else:
            self.is_udm = True
            self.addr = udm_addr
        self.login()

        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        requests.packages.urllib3.disable_warnings(SNIMissingWarning)
        requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

    @classmethod
    def new_from_environment(cls):
        apiendpoint = os.environ.get('API_URL', 'https://localhost:8443')
        apiisudm = int(os.environ.get('API_IS_UDM', 0))
        apiusername = os.environ.get('API_USERNAME', 'ubnt')
        apipassword = os.environ.get('API_PASSWORD', 'ubnt')

        if apiendpoint is None:
            raise AssertionError('API/URL is required in configuration')
        if apiusername is None or apipassword is None:
            raise AssertionError('API/Username and API/Password is required in configuration')

        if apiisudm:
            return cls(apiusername, apipassword, udm_addr=apiendpoint)
        else:
            return cls(apiusername, apipassword, controller_addr=apiendpoint)

    '''
    Unifi API endpoints are described in wiki:
        (https://ubntwiki.com/products/software/unifi-controller/api)
    '''
    def api_addr(self, endpoint):
        if self.is_udm:
            if endpoint == "login":
                return f'{self.addr}/api/auth/{endpoint}'
            elif endpoint == "status":
                return f'{self.addr}/proxy/network/{endpoint}'
            else:
                return f'{self.addr}/proxy/network/api/{endpoint}'
        else:
            if endpoint == "status":
                return f'{self.addr}/{endpoint}'
            else:
                return f'{self.addr}/api/{endpoint}'


    def clear_session(self):
        self.session.cookies.clear()

    def api_process_response(self, r):
        # Will raise exceptions if failing
        self.set_error(r)
        # parse json output
        data = r.json()
        return data

    def api_post(self, endpoint, payload):
        logging.debug(f'API POST {self.api_addr(endpoint)}')
        try:
            r = self.session.post(self.api_addr(endpoint), headers=self.api_headers, json=payload, verify=False, timeout=1)
            return self.api_process_response(r)
        except UniFiLoginRequiredException as e:
            if endpoint != 'login':
                self.login()
                r = self.session.post(self.api_addr(endpoint), headers=self.api_headers, json=payload, verify=False, timeout=1)
                return self.api_process_response(r)
            else:
                raise e


    def api_get(self, endpoint):
        logging.debug(f'API GET {endpoint}')
        try:
            r = self.session.get(self.api_addr(endpoint), headers=self.api_headers, verify=False, timeout=1)
            return self.api_process_response(r)
        except UniFiLoginRequiredException as e:
            self.login()
            r = self.session.get(self.api_addr(endpoint), headers=self.api_headers, verify=False, timeout=1)
            return self.api_process_response(r)


    def set_error(self, r):
        if r.status_code == 401:
            raise UniFiLoginRequiredException(f"HTTP Status Code: {r.status_code}")
        elif r.status_code != 200:
            raise UniFiException(f"HTTP Status Code: {r.status_code}")

        data = r.json()
        if 'meta' in data:
            if data['meta']['rc'] == 'ok':
                return
            elif data['meta']['rc'] == 'error':
                raise UniFiException(data['meta']['msg'])
            else:
                raise UniFiException(None, 'FAIL: \n' + pprint.pformat(data))

    def login(self):
        # https://hemma:8443/api/login
        # > POST {"username":"ubnt","password":"ubnt","strict":true}:
        # < Set-Cookie: unifises=k8U3umwhciVfp8e43evU95mwQI3eAxK3; Path=/; Secure; HttpOnly
        # < Set-Cookie: csrf_token=k8U3umwhciVfp8e43evU95mwQI3eAxK3; Path=/; Secure
        # { "data" : [ ] , "meta" : { "rc" : "ok"}}
        logging.info(f'Login {self.addr} {self.username}')
        payload = { 'username': self.username, 'password': self.password }
        self.api_post('login', payload)

    def sites(self):
        # https://hemma:8443/api/self/sites
        # { "data" : [ { "_id" : "56c87bc1b41038d25762ce86" , "attr_hidden_id" : "default" , "attr_no_delete" : true , "desc" : "Default" , "name" : "default" , "num_ap" : 2 , "num_sta" : 22 , "role" : "admin"}] , "meta" : { "rc" : "ok"}}
        data = self.api_get('self/sites')
        ret = []
        for s in data.get('data'):
            ret.append(site.Site(self, s))
        return ret
