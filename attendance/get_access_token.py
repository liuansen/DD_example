# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import json
import requests
import settings

from sqlalchemy import create_engine
from db import AccessToken
from sqlalchemy.orm import sessionmaker


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


if __name__ == '__main__':
    engine = create_engine(settings.MYSQL_CONNECT)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    access_tokens = get_access_token()
    new_access_token = session.query(AccessToken).filter_by(id='1').first()
    new_access_token.access_token = access_tokens
    session.commit()
    session.close()
