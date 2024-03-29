# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser

config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'conf/conf.ini')

class GetConf:
    def __init__(self, config_path=config_path):
        self.config = ConfigParser()
        self.config.read(config_path, encoding='utf-8')

    def __check_value(self, section, key):
        return self.config and self.config.has_option(section, key)

    def get_sections(self):
        return self.config.sections()

    def get_config(self, section, key, default=None):
        if self.__check_value(section, key):
            return self.config.get(section, key)
        else:
            return default

    def get_int(self, section, key, default=None):
        if self.__check_value(section, key):
            return int(self.get_config(section, key, default))
        else:
            return int(default)

    def get_items(self, section):
        return dict(self.config.items(section))

    def get_array(self, section, key):
        res = []
        if self.__check_value(section, key):
            res = eval(self.get_config(section, key))
        return res

if __name__ == '__main__':
    print(GetConf().get_config("server", "port"))