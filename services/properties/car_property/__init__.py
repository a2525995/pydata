# -*- coding: utf-8 -*-

import random

from .. import Provider as BaseProvider


class Provider(BaseProvider):
    list_plate = ['闽A', '闽D', '闽B', '闽G', '闽C', '闽E', '闽H', '闽F', '闽J', '粤A', '粤F', '粤B', '粤C', '粤D', '粤E', '粤J', '粤G',
                  '粤K', '粤H', '粤L', '粤M', '粤N', '粤P', '粤Q', '粤R', '粤S', '粤T', '粤U', '粤V', '粤W', '京A', '京B', '京E', '京F',
                  '京G', '津A', '津B', '津E', '津A', '津A', '冀A', '冀B', '冀C', '冀D', '冀E', '冀F', '冀G', '冀H', '冀J', '冀R', '冀T',
                  '晋A', '晋B', '晋C', '晋D', '晋E', '晋F', '晋K', '晋M', '晋H', '晋L', '晋J', '蒙A', '蒙B', '蒙C', '蒙D', '蒙G', '蒙K',
                  '蒙E', '蒙L', '蒙J', '蒙F', '蒙H', '蒙M', '辽A', '辽B', '辽C', '辽D', '辽E', '辽F', '辽G', '辽H', '辽J', '辽K', '辽L',
                  '辽M', '辽N', '辽P', '吉A', '吉B', '吉C', '吉D', '吉E', '吉F', '吉J', '吉G', '吉H', '黑A', '黑B', '黑G', '黑H', '黑J',
                  '黑E', '黑F', '黑D', '黑K', '黑C', '黑N', '黑M', '黑P', '沪R', '苏A', '苏B', '苏C', '苏D', '苏E', '苏F', '苏G', '苏H',
                  '苏J', '苏K', '苏L', '苏M', '苏N', '皖A', '皖B', '皖C', '皖D', '皖E', '皖F', '皖G', '皖H', '皖J', '皖M', '皖K', '皖L',
                  '皖N', '皖S', '皖R', '皖P', '浙A', '浙B', '浙C', '浙F', '浙E', '浙D', '浙G', '浙H', '浙L', '浙J', '浙K', '赣A', '赣H',
                  '赣J', '赣G', '赣K', '赣L', '赣B', '赣D', '赣C', '赣F']

    def genPlateNum(self):
        plateStr = random.choice(self.list_plate)
        plateItems = ['0', 'A', '1', 'B', '2', 'C', '3', 'D', '4', 'E', '5', 'F', '6', 'G', '7', 'H', '8', 'J', '9',
                      '0', 'K', '1', 'L', '2', 'M', '3', 'N', '4', 'P', '5', 'Q', '6', 'R', '7', 'S', '8', 'T', '9',
                      'U', '7', 'V', '5', 'W', '3', 'X', '9', 'Y', '2', 'Z']
        plateStr = ''.join([plateStr, plateItems[random.randint(0, len(plateItems) - 1)],
                            plateItems[random.randint(0, len(plateItems) - 1)],
                            plateItems[random.randint(0, len(plateItems) - 1)],
                            plateItems[random.randint(0, len(plateItems) - 1)],
                            plateItems[random.randint(0, len(plateItems) - 1)]])
        return ['plate_num', plateStr]
