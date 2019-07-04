# -*- coding: utf-8 -*-

import time, datetime
import requests, json
from faker import Factory
from faker.utils.loading import find_available_providers
from importlib import import_module

META_PROVIDERS_MODULES = [
    "faker.providers",
    "services.properties",
]

PROVIDERS = find_available_providers(
    [import_module(path) for path in META_PROVIDERS_MODULES])

fake = Factory.create(providers=PROVIDERS)


class CommonFunc:
    def deal_with_time(self, input_time_str):
        return datetime.datetime.strptime(input_time_str, "%Y-%m-%d %H:%M:%S")

    def deal_time(self, timestr):
        return int(time.mktime(time.strptime(timestr, "%Y-%m-%d %H:%M:%S")))

    def deal_with_num(self, loopnum):
        return int(loopnum)

    def user_check(self, user_id, user_pass, url):
        headers = {'Content-Type': 'application/json'}
        values = json.dumps({'username': user_id, 'password': user_pass})
        url = url + "/user/login"
        r = requests.post(url=url, headers=headers, data=values).json()
        return r

    def deal_with_relations(self, relations):
        if len(relations['entity']) == 0 and len(relations['events']) >= 1:
            relations['entity'].append('人')
        ret_relations = []
        # relation_list = re.sub(r"\W", ",", relations).split(",")
        for entity in relations["entity"]:
            if entity == "人":
                ret_relations.append(fake.person)
        for relation in relations["events"]:
            if relation == "乘车事件":
                ret_relations.append(fake.train_related)
            elif relation == "住宿事件":
                ret_relations.append(fake.hotel_related)
            elif relation == "航班事件":
                ret_relations.append(fake.flight_related)
            elif relation == "通话事件":
                ret_relations.append(fake.call_related)
            elif relation == "快递事件":
                ret_relations.append(fake.delivery_related)
            elif relation == "网吧事件":
                ret_relations.append(fake.inter_related)
            elif relation == "案件事件":
                ret_relations.append(fake.case_related)
            elif relation == "银行卡":
                ret_relations.append(fake.credit_related)
        return ret_relations

    def deal_with_property(self, properties):
        ret_properties = []
        for property in properties:
            if property == "身份证":
                ret_properties.append(fake.gen_id_number)
            elif property == "时间":
                ret_properties.append(fake.get_start_end)
            elif property == "酒店":
                ret_properties.append(fake.get_hotel)
            elif property == "地址":
                ret_properties.append(fake.get_address)
            elif property == "姓名":
                ret_properties.append(fake.gen_ch_name)
            elif property == '手机号':
                ret_properties.append(fake.gen_phone_number)
            elif property == '民族':
                ret_properties.append(fake.gen_minzu)
            elif property == '网吧':
                ret_properties.append(fake.gen_inter)
            elif property == '火车站':
                ret_properties.append(fake.gen_train_station)
            elif property == '机场':
                ret_properties.append(fake.gen_airport)
            elif property == '护照':
                ret_properties.append(fake.gen_passport)
            elif property == '英文名':
                ret_properties.append(fake.gen_en_name)
            elif property == '重点人类别':
                ret_properties.append(fake.get_seven_tag)
            elif property == '国籍':
                ret_properties.append(fake.gen_nation)
            elif property == '派出所':
                ret_properties.append(fake.gen_police_station)
            elif property == 'IP':
                ret_properties.append(fake.gen_ip)
            elif property == '航空公司':
                ret_properties.append(fake.gen_flight_company)
            elif property == '学历':
                ret_properties.append(fake.gen_education)
            elif property == '血型':
                ret_properties.append(fake.gen_blood)
            elif property == '车次':
                ret_properties.append(fake.gen_train_num)
            elif property == '单位':
                ret_properties.append(fake.gen_company)
            elif property == '邮件':
                ret_properties.append(fake.gen_email)
        return ret_properties

    def pro_time(self, a):
        return int(time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S")))
