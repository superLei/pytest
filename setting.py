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


BIZ_CONFIF = {"shop", "bargain", "internal", "marketing", "supply_chain"}
