# -*- coding: utf-8 -*-
# Author: Peng Jiachen
# @Time: 2019/6/27 7:39 PM
# @File: __init__.py.py
import datetime
import random
import time

from .. import Provider as BaseProvider
localized = False


class Provider(BaseProvider):
    def trans_time(self, time_str):
        return int(time.mktime(time.strptime(time_str, "%Y-%m-%d %H:%M:%S")))

    def get_start_end(self):
        start = self.trans_time("2019-04-01 00:00:00")
        end = self.trans_time("2019-07-01 00:00:00")
        times_stamp = time.localtime(random.randint(start, end))
        start_time = time.strftime("%Y-%m-%d %H:%M:%S", times_stamp)
        end_time = str(datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(
            minutes=random.randint(1, 10)))
        d = ['开始时间', start_time, '结束时间', end_time]
        return d

