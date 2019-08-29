# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import json

import requests

from Call_API import ApiClient
import settings


def get_access_token():
    """
    获取access_token
    :return:
    {
    "errcode": 0,
    "errmsg": "ok",
    "access_token": "fw8ef8we8f76e6f7s8df8s"
    }
    """
    url = 'https://oapi.dingtalk.com/gettoken?appkey={0}&appsecret={1}'.format(
        settings.APP_KEY, settings.APP_SECRET)
    r = requests.get(url)
    str_json = json.loads(r.text)
    access_token = str_json['access_token']
    return access_token


class RequestAPI(object):

    def __init__(self, access_token, url):
        self.access_token = access_token
        self.url = url

    def get_api(self):
        r = requests.get(self.url)
        str_json = json.loads(r.text)
        if str_json['errcode'] == 40041 or str_json['errmsg'] == '不合法的access_token':
            self.access_token = get_access_token()
            r = requests.get(self.url)
            str_json = json.loads(r.text)
        return str_json

    def post_api(self):
        pass


if __name__ == '__main__':
    req = RequestAPI(1, '12346')
    req.get_api()
