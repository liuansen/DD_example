# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import json
from datetime import date, datetime

import requests
import settings

from request_api import RequestAPI
from db import AccessToken
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Call_API import ApiClient


def select_access_token():
    engine = create_engine(settings.MYSQL_CONNECT)
    db_session = sessionmaker(bind=engine)
    session = db_session()
    token = session.query(AccessToken).filter(AccessToken.id == '1').one()
    return token.access_token


def get_dept_list_ids(access_token, dept_id):
    """
    获取子部门ID列表
    :return:
    {
    "errcode": 0,  # 返回码
    "errmsg": "ok",  # 对返回码的文本描述内容
    "sub_dept_id_list": [ 2,3,4,5 ]  # 子部门ID列表数据
    }
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
    {
    "errcode": 0,  # 返回码
    "errmsg": "ok", # 对返回码的文本描述内容
    "department": [
        {
           "id": 2, # 部门id
            "name": "钉钉事业部", # 部门名称
            "parentid": 1, # 部门名称
            "createDeptGroup": true, # 是否同步创建一个关联此部门的企业群，true表示是，false表示不是
            "autoAddUser": true # 当群已经创建后，是否有新人加入部门会自动加入该群, true表示是，false表示不是
        }
    ]
    }
    """
    url = 'https://oapi.dingtalk.com/department/list?access_token={0}'.format(access_token)
    r = requests.get(url)
    str_json = json.loads(r.text)
    return str_json


def get_dept_member(access_token, dept_id):
    """
    获取部门用户id列表
    :return:
    {
    "errcode": 0, # 返回码
    "errmsg": "ok",  # 对返回码的文本描述内容
    "userIds": ["1","2"]  # userid列表
    }
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
    "errcode": 0, # 返回码
    "errmsg": "ok",  # 对返回码的文本描述内容
    "hasMore": false, # 在分页查询时返回，代表是否还有下一页更多数据
    "userlist": [
        {
            "userid": "zhangsan", # 员工id
            "name": "张三" # 成员名称
        }
    ]
    }
    """
    url = 'https://oapi.dingtalk.com/user/simplelist?access_token={0}&department_id={1}'.format(
        access_token, dept_id
    )
    r = requests.get(url)
    str_json = json.loads(r.text)
    return str_json


def get_user_department_list(access_token, department_id):
    """
    获取部门用户详情
    https://oapi.dingtalk.com/user/listbypage?access_token=ACCESS_TOKEN&department_id=1
    :return:
    {
    "errcode": 0,
    "errmsg": "ok",
    "hasMore": false,
    "userlist":[
        {
            "userid": "zhangsan", # 员工在当前企业内的唯一标识，也称staffId。可由企业在创建时指定，并代表一定含义比如工号，创建后不可修改
            "unionid": "PiiiPyQqBNBii0HnCJ3zljcuAiEiE", #员工在当前开发者企业账号范围内的唯一标识，系统生成，固定值，不会改变
            "mobile": "1xxxxxxxxxx",  # 手机号
            "tel" : "xxxx-xxxxxxxx", # 分机号
            "workPlace" :"", # 办公地点
            "remark" : "", # 备注
            "order" : 1, # 表示人员在此部门中的排序，列表是按order的倒序排列输出的，即从大到小排列输出的
            "isAdmin": true,  #是否是企业的管理员，true表示是，false表示不是
            "isBoss": false, # 是否为企业的老板，true表示是，false表示不是
            "isHide": true, # 是否隐藏号码，true表示是，false表示不是
            "isLeader": true, # 	是否是部门的主管，true表示是，false表示不是
            "name": "张三", # 成员名称
            "active": true, # 表示该用户是否激活了钉钉
            "department": [1, 2], # 成员所属部门id列表
            "position": "工程师", # 职位信息
            "email": "test@xxx.com", # 员工的邮箱
            "avatar":  "xxx", # 头像url
            "jobnumber": "xxx", # 员工工号
            "extattr": {
                "爱好":"旅游",
                "年龄":"24"
                    }
            }
        ]
    }
    request.setDepartmentId(1L);
    request.setOffset(0L);
    request.setSize(10L);
    request.setOrder("entry_desc");
    request.setHttpMethod("GET");
    OapiUserListbypageResponse execute = client.execute(request,accessToken);
    """
    url = 'https://oapi.dingtalk.com/user/listbypage?access_token={0}&department_id={1}' \
          '&offset={2}&size={3}'.format(
        access_token, department_id, 0, 100)
    print(url)
    r = requests.get(url)
    str_json = json.loads(r.text)
    return str_json


def get_list_attendance(access_token, user_ids):
    """
    获取用户打卡记录
    :return:
        {
       "errmsg": "ok",
       "recordresult": [
        {
          "isLegal": "N",
          "baseCheckTime": 1492568460000,
          "id": 933202551,
          "userAddress": "北京市朝阳区崔各庄镇阿里中心.望京A座阿里巴巴绿地中心",
          "userId": "manager7078",
          "checkType": "OnDuty",
          "timeResult": "Normal",
          "deviceId": "cb7ace07d52fe9be14f4d8bec5e1ba79",
          "corpId": "ding7536bfee6fb1fa5a35c2f4657eb6378f",
          "sourceType": "USER",
          "workDate": 1492531200000,
          "planCheckTime": 1492568497000,
          "locationMethod": "MAP",
          "locationResult": "Outside",
          "userLongitude": 116.486888,
          "planId": 4550269081,
          "groupId": 121325603,
          "userAccuracy": 65,
          "userCheckTime": 1492568497000,
          "userLatitude": 39.999946,
          "procInstId": "cb992267-9b70"
        },
        {
          "isLegal": "N",
          "baseCheckTime": 1492568460000,
          "id": 991197412,
          "userAddress": "北京市朝阳区崔各庄镇阿里中心.望京A座阿里巴巴绿地中心",
          "userId": "manager7078",
          "checkType": "OnDuty",
          "timeResult": "Normal",
          "deviceId": "cb7ace07d52fe9be14f4d8bec5e1ba79",
          "corpId": "ding7536bfee6fb1fa5a35c2f4657eb6378f",
          "sourceType": "USER",
          "workDate": 1492531200000,
          "planCheckTime": 1492568497000,
          "locationMethod": "MAP",
          "locationResult": "Outside",
          "userLongitude": 116.486888,
          "planId": 4556390053,
          "groupId": 121325603,
          "userAccuracy": 65,
          "userCheckTime": 1492568497000,
          "userLatitude": 39.999946,
          "procInstId": "cb992267-9b70"
        }
      ],
      "errcode": 0
        }
    参数		            说明
    errcode          返回码
    errmsg           对返回码的文本描述内容
    id		        唯一标识ID
    groupId		    考勤组ID
    planId		    排班ID
    workDate		工作日
    corpId		    企业ID
    userId		    用户ID
    checkType	    考勤类型，
                    OnDuty：上班
                    OffDuty：下班
    sourceType	    数据来源，
                    ATM：考勤机;
                    BEACON：IBeacon;
                    DING_ATM：钉钉考勤机;
                    USER：用户打卡;
                    BOSS：老板改签;
                    APPROVE：审批系统;
                    SYSTEM：考勤系统;
                    AUTO_CHECK：自动打卡
    timeResult	    时间结果，
                    Normal：正常;
                    Early：早退;
                    Late：迟到;
                    SeriousLate：严重迟到；
                    Absenteeism：旷工迟到；
                    NotSigned：未打卡
    locationResult	    位置结果，
                        Normal：范围内
                        Outside：范围外，外勤打卡时为这个值
    approveId		关联的审批id，当该字段非空时，表示打卡记录与请假、加班等审批有关
    procInstId		关联的审批实例id，当该字段非空时，表示打卡记录与请假、加班等审批有关。可以与获取单个审批数据配合使用
    baseCheckTime	计算迟到和早退，基准时间；也可作为排班打卡时间
    userCheckTime	实际打卡时间
    classId		    考勤班次id，没有的话表示该次打卡不在排班内
    isLegal		    是否合法，当timeResult和locationResult都为Normal时，该值为Y；否则为N
    locationMethod	定位方法
    deviceId		设备id
    userAddress	    用户打卡地址
    userLongitude	用户打卡经度
    userLatitude	用户打卡纬度
    userAccuracy	用户打卡定位精度
    userSsid		用户打卡wifi SSID
    userMacAddr	    用户打卡wifi Mac地址
    planCheckTime	排班打卡时间
    baseAddress	    基准地址
    baseLongitude	基准经度
    baseLatitude	基准纬度
    baseAccuracy	基准定位精度
    baseSsid		基准wifi ssid
    baseMacAddr	    基准 Mac 地址
    outsideRemark	打卡备注
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
    access_token = select_access_token()
    # s = get_access_token()
    # print(s)
    # str_jsons = get_dept_member(access_token, 1)
    # user_ids = str_jsons['userIds']
    # user_ids = ['095125030120949661', '2429351850639093416', '293329500523750848']
    # get_list_attendance(access_token, user_ids)
    # str_jsons = get_user_simple_list(access_token, 1)
    # print(str_jsons)
    # k = get_dept_list(access_token)
    # print(k)
    s = get_user_department_list(access_token, 1)
    print(s)
