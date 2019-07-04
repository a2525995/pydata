# -*- coding: utf-8 -*-

from common.get_conf import GetConf


class InitCommon:
    c = GetConf()
    download_url = c.get_config('server', 'download_url')


