# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import json
from datetime import date, datetime

import requests

import settings
from Call_API import ApiClient


def get_access_token():
    """
    获取access_token
    :return:
    """
    url = 'https://oapi.dingtalk.com/gettoken?appkey={0}&appsecret={1}'.format(
        settings.APP_KEY, settings.APP_SECRET)
    r = requests.get(url)
    str_json = json.loads(r.text)
    access_token = str_json['access_token']
    return access_token


def get_dept_list_ids(access_token, dept_id):
    """
    获取子部门ID列表
    :return:
    """
    url = 'https://oapi.dingtalk.com/department/list_ids?access_token={0}&id={1}'.format(
        access_token, dept_id
    )
    r = requests.get(url)
    str_json = json.loads(r.text)
    return str_json


def get_dept_list(access_token):
    """
    获取部门列表
    https://oapi.dingtalk.com/department/list?access_token=ACCESS_TOKEN
    :return:
    """
    url = 'https://oapi.dingtalk.com/department/list?access_token={0}'.format(access_token)
    r = requests.get(url)
    str_json = json.loads(r.text)
    return str_json


def get_dept_member(access_token, dept_id):
    """
    获取部门用户id列表
    :return:
    """
    url = 'https://oapi.dingtalk.com/user/getDeptMember?access_token={0}&deptId={1}'.format(
        access_token, dept_id)
    r = requests.get(url)
    str_json = json.loads(r.text)
    return str_json


def get_user_simple_list(access_token, dept_id):
    """
    获取部门用户信息
    :return:
        {
        'errcode': 0,  # 返回码
        'department': [{
            'createDeptGroup': True, # 是否同步创建一个关联此部门的企业群，true表示是，false表示不是
            'name': '厦门OpenHappy科技有限公司', # 部门名称
            'id': 1,  # 部门id
            'autoAddUser': True
        }],
        'errmsg': 'ok'  # 对返回码的文本描述内容  # 当群已经创建后，是否有新人加入部门会自动加入该群, true表示是，false表示不是
    }
    """
    url = 'https://oapi.dingtalk.com/user/simplelist?access_token={0}&department_id={1}'.format(
        access_token, dept_id
    )
    r = requests.get(url)
    str_json = json.loads(r.text)
    return str_json


def get_list_attendance(access_token, user_ids):
    """
    获取用户打卡记录
    :return:
    """
    url = 'https://oapi.dingtalk.com/attendance/listRecord?access_token={0}'.format(access_token)
    today = date.today()
    from_date = '{0}-{1}-{2} 08:30:00'.format(today.year, today.month, today.day)
    to_date = '{0}-{1}-{2} 17:30:00'.format(today.year, today.month, today.day)
    data = {
        "userIds": user_ids,
        "checkDateFrom": from_date,
        "checkDateTo": to_date,
        "isI18n": "false"
    }
    cli = ApiClient(api_url=url)
    s = cli.call_api(data)
    return 0


if __name__ == '__main__':
    access_token = 'ffd08bd5388a306d9e67d2c982a6f0a6'
    # s = get_access_token()
    # print(s)
    # str_jsons = get_dept_member(access_token, 1)
    # user_ids = str_jsons['userIds']
    # user_ids = ['095125030120949661', '2429351850639093416', '293329500523750848']
    # get_list_attendance(access_token, user_ids)
    # str_jsons = get_user_simple_list(access_token, 1)
    # print(str_jsons)
    k = get_dept_list(access_token)
    print(k)
