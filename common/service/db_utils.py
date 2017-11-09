#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import unittest
import MySQLdb
from test_case import promotion_utils

from datetime import date, datetime

import sys

import setting
from common.module import mysql_module

class DbUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mysql_op = mysql_module.Mysql_Module()

    def test_case_1(self):
        # mysql_con2 = MySQLdb.connect('172.16.0.12','myshopcrmdev','mydev@pwd','db_shopcrm_002')
        # # 使用cursor()方法获取操作游标
        # cursor = mysql_con2.cursor()
        # # 使用execute方法执行SQL语句
        # cursor.execute('SELECT * FROM `db_shopcrm_002`.`tbl_promotion_master` WHERE groupID=11009')
        # # 使用 fetchone() 方法获取一条数据库。
        # data = cursor.fetchone()
        mysql_read = self.mysql_op.DataRead('SELECT * FROM `db_shopcrm_002`.`tbl_promotion_master` WHERE groupID=11009','dohko')
        # result = json.dumps(mysql_read[0],cls=AdvEncoder)
        # result['ruleJson'] = json.dumps(result['ruleJson'])

        print mysql_read[0]['ruleJson']


    def test_case_2(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        lst = ['a','b']
        d2.pop(lst)
        print d2
        print cmp(d,d2)
        food = {'actionStamp', 'createStamp', 'action'}
        self.util = promotion_utils.PromotionUtils()



class AdvEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return super.default(self, obj)

