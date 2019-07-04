# -*- coding: utf-8 -*-

import json
import multiprocessing
import threading
import time
from multiprocessing import Manager

from common.file_info import make_tar
from common.funcs import CommonFunc
from services.create_data import create_data_property, logger

common = CommonFunc()


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception as e:
            return e


def generate_data(arg):
    loop_num = common.deal_with_num(arg['loopnum'])
    relation = common.deal_with_property(arg["relations"])
    logger.debug('create_data params: {}-{}'.format(loop_num, relation))
    len_thread = 1
    time_str = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    final = []
    # """多线程"""
    # for i in range(len_thread):
    #     csv_dict = MyThread(create_data_property, (int(loop_num/len_thread), relation, start_time, end_time))
    #     csv_dict.start()
    #     csv_dict.join()
    #     result = csv_dict.get_result()
    #     time_str = str(int(time_str )+ 1)
    #     file_data = make_tar(result, time_str)
    #     file_url = file_data["file_url"]
    #     file_path_list = file_data["file_path_list"]
    #     ret_dic = {"cont": file_url, "file_path_list": file_path_list}
    #     final.append(ret_dic)
    # property_result = {"status": 200, "data": final}
    # return json.dumps(property_result)
    """多进程"""
    q = Manager()
    jobs = []
    for i in range(len_thread):
        res = q.dict()
        csv_dict = multiprocessing.Process(target=create_data_property,
                                           args=(int(loop_num / len_thread), relation, res))
        jobs.append(csv_dict)
        csv_dict.start()
        csv_dict.join()
        time_str = str(int(time_str) + 1)
        file_data = make_tar(res, time_str)
        file_url = file_data["file_url"]
        file_path_list = file_data["file_path_list"]
        ret_dic = {"cont": file_url, "file_path_list": file_path_list}
        final.append(ret_dic)
    property_result = {"status": 200, "data": final}
    return json.dumps(property_result)
