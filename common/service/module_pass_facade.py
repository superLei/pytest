# encoding = 'utf-8'

from common.module import idgenerate_module
from common.module.list_module import ListCmp
from common.module import md5_module
from common.module import timestampgenerate_module
from common.module.env_module import Env_Module
from common.module.testcase_module import MyTestCase
import time
from datetime import datetime

class Module_Pass:
    def __init__(self):
        pass

    def list_equals(self, list1, list2):
        return ListCmp().listEquals(list1, list2)

    def list_equals_byDictItemKeyList(self, dict, list, keyList):
        return ListCmp().listEqualsByDictItemKeyList(dict, list, keyList)

    def get_test_assertEqual(self, first, second, msg=None):
        return MyTestCase().assertEqual(first, second)

    def get_environment_url(self, sheet_index):
        env_url = Env_Module().get_env_url(sheet_index)
        return env_url

    def get_random_id(self):
        id = idgenerate_module.OrderIdGenerator()
        return id

    def get_uuid(self):
        uuid = idgenerate_module.UUidGenerator()
        return uuid

    def get_sign(self, **Date_input):
        sign = md5_module.get_sign(**Date_input)
        return sign

    def get_md5(self):
        md5 = md5_module.md5_module()
        return md5

    def get_timestamp(self):
        timestamp = timestampgenerate_module.TinmeStampGenerator()
        return timestamp

    def get_systemcurrenttime(self):
        now_time = timestampgenerate_module.SystemCurrentTime()
        return now_time

    def get_systemagotime(self):
        beforedate = timestampgenerate_module.SystemAgoTime()
        return beforedate

    def get_systemyesterdaytime(self):
        yesterdaydata = timestampgenerate_module.SystemYesterdayTime()
        return yesterdaydata

    def get_systemtomorrowtime(self):
        tomorrowdata = timestampgenerate_module.SystemTomorrowTime()
        return tomorrowdata
    def get_currentTime(self):
        return  time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

    def get_currentDate(self):
        return  time.strftime('%Y%m%d',time.localtime(time.time()))

    def get_currentTime2(self):
        dt = datetime.now()
        return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())) + str(dt.microsecond)

if __name__ == '__main__':
    print idgenerate_module.OrderIdGenerator()
    print timestampgenerate_module.TinmeStampGenerator()
    print timestampgenerate_module.SystemCurrentTime()
    print timestampgenerate_module.SystemAgoTime()