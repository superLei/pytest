#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import allure
import sys
import json
import time
from decimal import Decimal
from common.service import excel_case_facade
from common.service.module_pass_facade import Module_Pass
from common.service import str_utils
from common.module import mysql_module
import promotion_utils

sys.path.append("../../")
class Test_01(object):
    def setup_class(cls):
        _file_name = 'test_saas'
        cls.filename = "../data/%s.xlsx" % _file_name
        cls.promotionUtils = promotion_utils.PromotionUtils()
        cls.excel_facade = excel_case_facade.GetExcelCaseDate()
        cls.str_util = str_utils.StrUtils()

        # 实例化数据库对象
        cls.mysql_op = mysql_module.Mysql_Module()
        global coo,sheet_index
        coo = cls.promotionUtils._login()
        print coo
        sheet_index = 18
        global startDate
        startDate = Module_Pass().get_currentDate()

   #

    @allure.feature('【累计次数赠送】:每累计2次，送2份，验证卡请求正确次数(如:1)下参与活动,并计算活动后的各金额')
    def test_01(self):
        # 获取券类别id
        sql_giftItemID = 'SELECT giftItemID FROM `tbl_crm_gift` WHERE groupID = 11009'
        db_giftItemID = self.mysql_op.DataRead(sql_giftItemID, 'dohko')
        # 请求基础营销发劵接口
        d = {}
        giftItem = self.promotionUtils._giftItem(d, sheet_index, 1)
        for i in range(len(giftItem[1]['giftList'])):
            sql_itemID = 'select * from `tbl_crm_customer_giftDetail` where itemID=' + str(giftItem[1]['giftList'][i]['giftCustomerID'])
            print sql_itemID
            db_result = self.mysql_op.DataRead(sql_itemID, 'dohko')
            print db_result
            # assert db_result[0] != None










