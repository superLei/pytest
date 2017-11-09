# coding:utf-8
import logging
import os
import inspect
import time

'''
Logging Config
'''
file_path = inspect.stack()[0][1]
cwd = os.path.split(file_path)[0]
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s '
           '%(filename)s '
           '%(funcName)s '
           '[line:%(lineno)d] '
           '%(levelname)s '
           ':%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename="%s/log/%s.log" % (cwd, time.strftime("%y-%m-%d")),
    filemode='a'
)

'''
ENVIRONMENT CONFIG
'''
ENVIRONMENT_CONFIG = {
    "dohko": {
        "saasserver": "http://192.168.4.75:8090",
        "crm": "http://dohko.crm.shop.hualala.com",
        # "crm": "http://dohko.crm.shop.hualala.com",
        "login": "http://dohko.login.hualala.com:31251",
        "admin": "http://dohko.admin.hualala.com",
        "getShopPromotionByDate":"http://dohko.api.promotion21.service.hualala.com",
        "delgroup":"http://dohko.api.promotion21.service.hualala.com",
        "promotion_v2":"http://dohko.api.promotion21.service.hualala.com",
        "queryTransNum":"http://dohko.api.promotion21.service.hualala.com"
        # "promotion_v2":"http://192.168.19.132:8880"
    },
    "test": {
        "crm": "http://dohko.crm.shop.hualala.com",
        "login": "http://dohko.login.hualala.com:31251",
        "admin": "http://dohko.admin.hualala.com",
        "getShopPromotionByDate":"http://dohko.api.promotion21.service.hualala.com",
        "delgroup":"http://172.16.32.35:8880",
        "promotion_v2":"http://172.16.32.35:8880",
        "queryTransNum":"http://172.16.32.35:8880"
    }
}

CASE_REFERENCE = {
    "testlink": "testlink.hualala.com",
    "excel": "excel"
}

EMAIL_CONFIG = {

}

TESTLINK_CONFIG = {
    "url": "http://testlink.hualala.com/testlink/lib/api/xmlrpc/v1/xmlrpc.php",
    "key": "00276ea6fb5bda36590156fe752013b5"
}

REQUEST_HEADER = {
    'content-type': "application/x-www-form-urlencoded"
}
REQUEST_HEADER2 = {
    'content-type': "application/json"
}

MYSQL_CONFIG = {
    "dohko": {"host": "172.16.0.12",
              "user": "myshopcrmdev",
              "passwd": "mydev@pwd",
              "port": 3306,
              "db": "db_shopcrm_002",
              'charset': 'utf8'},
    "mock": {"host": "172.16.32.39",
             "user": "root",
             "passwd": "123456",
             "port": 3306,
             "db": "mock",
             'charset': 'utf8'}
}

BIZ_CONFIF = {"shop", "bargain", "internal", "marketing", "supply_chain"}
