# -*- coding: utf-8 -*-

import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
import time
from services.generate_property import generate_data, logger
from configparser import ConfigParser

parser = ConfigParser()
conf_path = os.path.join(path, "local_create/conf/conf.ini")
parser.read(conf_path, encoding='utf-8')
loop_num, properties = None, None
# 获取文件参数
try:
    loop_num = int(parser.get("conf", "loop_num"))
except:
    logger.debug("No loopnum_num input")

# 拼事件json串
try:
    properties = parser.get("conf", "property").split(",")
except:
    logger.debug("No properties input")

arg = {'loopnum': loop_num, 'relations': properties}
# 生成事件
t = time.time()
generate_data(arg)
print((time.time() - t))
