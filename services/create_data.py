# -*- coding: UTF-* -*-


import time
from itertools import chain

from common.funcs import fake
from common.make_log import logs

logger = logs()


# def create_data_property(loop_num, property_methods=None, from_datetime=None, to_datetime=None):
def create_data_property(loop_num, property_methods=None, csv_dict=None):
    try:
        final, header, data = [], [], []
        logger.debug(
            "create_data_property params ---> loop_num: {}, property_methods: {}".format(
                loop_num, property_methods))
        if len(property_methods) == 0:
            property_methods = [fake.gen_id_number, fake.get_address, fake.gen_phone_number,
                                fake.get_start_end, fake.get_hotel, fake.gen_ch_name]
        for _ in range(loop_num):
            a = (method() for method in property_methods)  # 生成一个大的列表a，里面包含多个子列表
            tmp_list = list(chain(*a))  # 合并a中的所有子列表
            # tmp_list = list(chain(*method(from_datetime,to_datetime)) for method in property_methods)
            header = tmp_list[::2]  # 获取tmp_list的奇数位的值，即获取所有的header
            data = tmp_list[1::2]  # 获取tmp_list的偶数位的值，即获取所有的属性值
            final.append(data)
        final.append(header)
        csv_dict['property'] = final[::-1]
        return csv_dict
    except ValueError:
        logger.debug("Request params error, loop_num-{},property_methods-{}".format(loop_num, property_methods))
