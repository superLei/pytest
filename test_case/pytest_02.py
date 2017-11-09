#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import allure
import sys
import math
import json
from common.service import excel_case_facade
from common.service.module_pass_facade import Module_Pass
from common.service import str_utils
import promotion_utils

sys.path.append("../../")
class Test_02(object):
    def setup_class(cls):
        _file_name = 'test_saas'
        cls.filename = "../data/%s.xlsx" % _file_name
        cls.promotionUtils = promotion_utils.PromotionUtils()
        cls.excel_facade = excel_case_facade.GetExcelCaseDate()
        cls.str_util = str_utils.StrUtils()
        global coo,sheet_index
        sheet_index = 15
        coo = cls.promotionUtils._login()
        global startDate
        startDate = Module_Pass().get_currentDate()

    @allure.feature('【团购券测试点】:禁用活动,再启用,验证此活动规则下参与优惠')
    def test_29(self):
        d = {
            "ruleJson": {"giftValue": "100", "points": "1", "targetScope": "0", "voucherVerify": "0", "costIncome": "1",
                         "evidence": "0", "stageType": "2", "giftPrice": "1", "voucherVerifyChannel": "1",
                         "blackList": False, "stage": [{"stageAmount": "0", "giftMaxUseNum": 1}], "transFee": "0"}}
        foodLst = {"price": 100.1, "count": 1}
        # 删除所有活动
        self.promotionUtils._del_all_promotion_v2()
        # 添加活动
        add_promotions = self.promotionUtils._add_promotions(d, sheet_index, 10, coo=coo)
        # 编辑活动
        edit_json = {"promotionID": add_promotions[0]}
        enable_promotions = self.promotionUtils._enable_promotions(edit_json, sheet_index, 25, coo=coo)
        edit_json = {"promotionID": add_promotions[0],"isActive": "ACTIVE"}
        enable_promotions = self.promotionUtils._enable_promotions(edit_json, sheet_index, 25, coo=coo)
        # 清除缓存
        self.promotionUtils._clear_info_cache_v2(startDate)
        print "***这是第[1]条请求sass营销计算接口***"
        # 执行计算接口
        execute_promotions = self.promotionUtils._execute_promotions(foodLst, sheet_index, 22)

        print('***这是第1条测试,price/count为:[{0}元,{1}份]***'.format(foodLst.get('price'), foodLst.get('count')))

        # 检验菜品count
        assert execute_promotions[0]['programLst'][0]['foodLst'][0]['count'] == foodLst.get('count')
        # 检验菜品price
        assert execute_promotions[0]['programLst'][0]['foodLst'][0]['price'] == foodLst.get('price')
        # 检验菜品payPrice
        assert execute_promotions[0]['programLst'][0]['foodLst'][0]['payPrice'] == foodLst.get('price')
        # 校验账单的优惠金额
        assert execute_promotions[0]['programLst'][0]['promotionAmount'] == 99
        # 校验单个菜品的实收金额

        assert execute_promotions[0]['programLst'][0]['foodLst'][0]['payTotal'] == 1.1
        # 校验账单的实收金额

        assert execute_promotions[0]['programLst'][0]['receivableAmount'] == 1.1
        # 校验菜品的活动id（bill类型的不检验）
        # assert execute_promotions[0]['programLst'][0]['foodLst'][0]['promotionList'][0] == add_promotions[0]
        # 校验活动promotionID
        assert execute_promotions[0]['programLst'][0]['promotion']['promotionID'] == add_promotions[0]
        # 检验活动名称
        print add_promotions[2]['promotionName']
        assert execute_promotions[0]['programLst'][0]['promotion']['promotionName'].encode('utf-8') == \
               add_promotions[2]['promotionName'].encode('utf-8')
        # 检验活动类别名称
        assert execute_promotions[0]['programLst'][0]['promotion']['categoryName'].encode('utf-8') == add_promotions[2][
            'categoryName'].encode('utf-8')
        # 检验活动类别
        assert execute_promotions[0]['programLst'][0]['promotion']['promotionType'] == add_promotions[2][
            'promotionType']
        # 检验活动promotionCode
        assert execute_promotions[0]['programLst'][0]['promotion']['promotionCode'] == add_promotions[1]
        # 检验programType(10-->营销活动)
        assert execute_promotions[0]['programLst'][0]['programType'] == 10
        # 检验菜品名称foodName
        assert execute_promotions[0]['programLst'][0]['foodLst'][0]['foodName'] == execute_promotions[1]['foodLst'][0][
            'foodName']
        # 检验菜品单位
        assert execute_promotions[0]['programLst'][0]['foodLst'][0]['foodUnit'] == execute_promotions[1]['foodLst'][0][
            'foodUnit']
        # 检验菜品类别
        assert execute_promotions[0]['programLst'][0]['foodLst'][0]['foodCategoryName'] == \
               execute_promotions[1]['foodLst'][0][
                   'foodCategoryName']
        # 菜品的活动标识
        assert execute_promotions[0]['programLst'][0]['foodLst'][0]['sequenceID'] == \
               execute_promotions[1]['foodLst'][0][
                   'sequenceID']
        assert execute_promotions[0]['programLst'][0]['foodLst'][0]['fromSequenceID'] == \
               execute_promotions[1]['foodLst'][0][
                   'fromSequenceID']
        # 参加活动的菜品的id列表
        assert execute_promotions[0]['programLst'][0]['foodOrderKeys'][0] == execute_promotions[1]['foodLst'][0][
            'sequenceID']
        # 团购券信息
        assert execute_promotions[0]['programLst'][0]['promotion']['vouchGroup']['voucherPrice'] == round(
            float(add_promotions[2]['ruleJson']['giftPrice']), 2)
        assert execute_promotions[0]['programLst'][0]['promotion']['vouchGroup']['voucherValue'] == round(
            float(add_promotions[2]['ruleJson']['giftValue']), 2)
        assert execute_promotions[0]['programLst'][0]['promotion']['vouchGroup']['transFee'] == round(
            float(add_promotions[2]['ruleJson']['transFee']), 2)
        assert execute_promotions[0]['programLst'][0]['promotion']['vouchGroup']['maxUseCount'] == 1
        assert execute_promotions[0]['programLst'][0]['promotion']['vouchGroup']['groupIncome'] == 1
        assert execute_promotions[0]['programLst'][0]['promotion']['vouchGroup']['costIncome'] == round(
            float(add_promotions[2]['ruleJson']['costIncome']), 2)
        assert execute_promotions[0]['programLst'][0]['promotion']['vouchGroup']['voucherVerify'] == round(
            float(add_promotions[2]['ruleJson']['voucherVerify']), 2)
        assert execute_promotions[0]['programLst'][0]['promotion']['vouchGroup']['voucherVerifyChannel'] == round(
            float(add_promotions[2]['ruleJson']['voucherVerifyChannel']), 2)
        assert execute_promotions[0]['programLst'][0]['promotion']['vouchGroup']['points'] == round(
            float(add_promotions[2]['ruleJson']['points']), 2)
        assert execute_promotions[0]['programLst'][0]['promotion']['vouchGroup']['evidence'] == round(
            float(add_promotions[2]['ruleJson']['evidence']), 2)


