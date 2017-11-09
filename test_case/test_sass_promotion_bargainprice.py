#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import allure
import json
from data import get_current_path
from common.service import excel_case_facade
from common.service.module_pass_facade import Module_Pass
from common.service import str_utils
import promotion_utils


class Test_BargainPrice(object):
    def setup_class(cls):
        _file_name = '/test_saas.xlsx'
        _file_path = get_current_path.get_cur_path()
        cls.filename = _file_path + _file_name
        print _file_path
        cls.promotionUtils = promotion_utils.PromotionUtils()
        cls.excel_facade = excel_case_facade.GetExcelCaseDate()
        cls.str_util = str_utils.StrUtils()
        global coo
        coo = cls.promotionUtils._login()
        global startDate
        startDate = Module_Pass().get_currentDate()

    @allure.feature('数据准备:特价菜')
    def test_1(self):
        # 删除所有活动
        self.promotionUtils._del_all_promotion_v2()
        # 清除缓存
        self.promotionUtils._clear_info_cache_v2(startDate)
        global lst_bargainprice, lst_promotionid, lst_promotioncode, lst_price, lst_response
        lst_bargainprice = [21,22,233.2,23.5,10.19,5.0,66666]
        lst_price = [21.5,88.8,233.3,23.6,10.2,5.1,66666.6]
        lst_response = []
        lst_promotionid = []
        lst_promotioncode = []
        for i in range(0, len(lst_price)):
            # 获取excel中的请求数据
            getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=5, row_id=1)
            # 处理excel中的请求数据
            tmp_result = json.loads(getInputData)
            tmp_result['priceLst'][0]['price'] = lst_bargainprice[i]
            tmp_result['priceLst'] = json.dumps(tmp_result['priceLst'])
            promotionCode = Module_Pass().get_currentTime2()
            tmp_result['promotionCode'] = promotionCode
            lst_promotioncode.append(promotionCode)
            # 获取结果
            result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=5, row_id=1, data=tmp_result,
                                                         coo=coo)
            # 从结果中获取响应信息
            result_response = json.loads(result[1][0])
            lst_promotionid.append(result_response['data']['promotionIDStr'])
            # 从结果中获取excel中期望结果的数据
            result_excel = json.loads(result[0])
            # 进行接口结果断言
            assert result_response['code'] == result_excel['code']

            print "***这是第[" + str(i) + "]条请求sass营销计算接口***"
            # 获取excel中的请求数据
            getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=5, row_id=4)
            # 处理excel中的请求数据
            tmp_result = json.loads(getInputData)
            tmp_result['foodLst'][0]['count'] = str(lst_price[i])  # 菜品数量
            tmp_result['foodLst'][0]['price'] = str(lst_price[i])  # 菜品价格
            # 获取结果
            result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=5, row_id=4, data=tmp_result)
            # 从结果中获取响应信息
            result_response = json.loads(result[1][0])
            lst_response.append(result_response)
            # 从结果中获取excel中期望结果的数据
            result_excel = json.loads(result[0])
            # 进行接口结果断言
            assert result_response['code'] == result_excel['code']

            # 删除所有活动
            self.promotionUtils._del_all_promotion_v2()
            # 清除缓存
            self.promotionUtils._clear_info_cache_v2(startDate)

    @allure.feature('特价菜计算测试')
    def test_2(self):
        # 校验活动打折的金额
        for i in range(0, len(lst_response)):
            print "***这是第[" + str(i) + "]条测试.price/count:[" + str(lst_price[i]) + "],菜品特价为:[" + str(
                lst_bargainprice[i]) + "]***"
            # 校验折扣的金额(小数位取两位，抹掉其余位)

            promotionAmount = round(lst_price[i] * lst_price[i] - lst_bargainprice[i] * lst_price[i],
                                    2)  # 整数相除为0 ，如果是浮点数除法则执行精确除法。
            # print "计算后的折扣金额是：" + str(lst_price[i] * lst_price[i] * (1 - lst_bargainprice[i] / 10.0))
            origin_promotionAmount = lst_response[i]['programLst'][0]['promotionAmount']
            assert origin_promotionAmount == promotionAmount
            # 校验实收金额
            receivableAmount = round(lst_bargainprice[i] * lst_price[i],
                                     2)  # float类型,4-3.6后精度丢失得0.39999999
            assert lst_response[i]['programLst'][0]['receivableAmount'] == receivableAmount
            # 校验未折扣的金额
            assert lst_response[i]['programLst'][1]['promotionAmount'] == 0
            # 校验未折扣的实收金额
            receivableAmount = round(lst_price[i] * lst_price[i], 2)
            assert lst_response[i]['programLst'][1]['receivableAmount'] == receivableAmount
            # 校验promotionID
            assert lst_response[i]['programLst'][0]['promotion']['promotionID'] == lst_promotionid[i]
            # 检验活动类别
            assert lst_response[i]['programLst'][0]['promotion']['categoryName'].encode('utf-8') == '特价菜angle'
            # 检验活动promotionCode
            assert lst_response[i]['programLst'][0]['promotion']['promotionCode'] == lst_promotioncode[i]
            # 检验programType(10-->营销活动)
            assert lst_response[i]['programLst'][0]['programType'] == 10
            # 检验菜品count
            assert lst_response[i]['programLst'][0]['foodLst'][0]['count'] == lst_price[i]
            # 检验菜品price
            assert lst_response[i]['programLst'][0]['foodLst'][0]['count'] == lst_price[i]
            # 检验菜品名称foodName
            assert lst_response[i]['programLst'][0]['foodLst'][0]['foodName'].encode('utf-8') == '鱼香肉丝'

    @allure.feature('异常数据准备:特价菜;请求营销计算接口')
    def test_3(self):
        # 删除所有活动
        self.promotionUtils._del_all_promotion_v2()
        # 清除缓存
        self.promotionUtils._clear_info_cache_v2(startDate)
        global lst_bargainprice2, lst_promotionid2, lst_promotioncode2, lst_price2, lst_response2
        lst_bargainprice2 = [21.5, 88.8, 233.3, 23.6, 10.2, 5.1, 66666.6]
        lst_price2 = [21, 22, 233.2, 23.5, 10.1, 5.0, 66666]
        lst_response2 = []
        lst_promotionid2 = []
        lst_promotioncode2 = []
        for i in range(0, len(lst_price2)):
            # 获取excel中的请求数据
            getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=5, row_id=1)
            # 处理excel中的请求数据
            tmp_result = json.loads(getInputData)
            tmp_result['priceLst'][0]['price'] = lst_bargainprice2[i]
            tmp_result['priceLst'] = json.dumps(tmp_result['priceLst'])
            promotionCode = Module_Pass().get_currentTime2()
            tmp_result['promotionCode'] = promotionCode
            lst_promotioncode2.append(promotionCode)
            # 获取结果
            result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=5, row_id=1, data=tmp_result,
                                                         coo=coo)
            # 从结果中获取响应信息
            result_response = json.loads(result[1][0])
            lst_promotionid2.append(result_response['data']['promotionIDStr'])
            # 从结果中获取excel中期望结果的数据
            result_excel = json.loads(result[0])
            # 进行接口结果断言
            assert result_response['code'] == result_excel['code']

            print "***这是第[" + str(i) + "]条请求sass营销计算接口***"
            # 获取excel中的请求数据
            getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=5, row_id=4)
            # 处理excel中的请求数据
            tmp_result = json.loads(getInputData)
            tmp_result['foodLst'][0]['count'] = str(lst_price2[i])  # 菜品数量
            tmp_result['foodLst'][0]['price'] = str(lst_price2[i])  # 菜品价格
            # 获取结果
            result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=5, row_id=4, data=tmp_result)
            # 从结果中获取响应信息
            result_response = json.loads(result[1][0])
            lst_response2.append(result_response)
            # 从结果中获取excel中期望结果的数据
            result_excel = json.loads(result[0])
            # 进行接口结果断言
            assert result_response['code'] == result_excel['code']

            # 删除所有活动
            self.promotionUtils._del_all_promotion_v2()
            # 清除缓存
            self.promotionUtils._clear_info_cache_v2(startDate)

    @allure.feature('异常测试：特价菜计算测试')
    def test_4(self):
        # 校验活动打折的金额
        for i in range(0, len(lst_response2)):
            print "***这是第[" + str(i) + "]条测试.price/count:[" + str(lst_price2[i]) + "],菜品特价为:[" + str(
                lst_bargainprice2[i]) + "]***"
            # 校验折扣的金额(小数位取两位，抹掉其余位)
            promotionAmount = 0
            origin_promotionAmount = lst_response2[i]['programLst'][0]['promotionAmount']
            assert origin_promotionAmount == promotionAmount
            # 校验实收金额
            receivableAmount = round(lst_price2[i] * lst_price2[i],
                                     2)  # float类型,4-3.6后精度丢失得0.39999999
            assert lst_response2[i]['programLst'][0]['receivableAmount'] == receivableAmount
            # 校验未折扣的金额
            assert lst_response2[i]['programLst'][0]['promotionAmount'] == 0
            # 校验未折扣的实收金额
            receivableAmount = round(lst_price2[i] * lst_price2[i], 2)
            assert lst_response2[i]['programLst'][0]['receivableAmount'] == receivableAmount
            # 校验promotionID
            assert lst_response2[i]['programLst'][0]['promotion']['promotionID'] == '0'
            # 检验活动类别
            assert lst_response2[i]['programLst'][0]['promotion']['categoryName'].encode('utf-8') == '不参加优惠'
            # 校验promotionName
            assert lst_response2[i]['programLst'][0]['promotion']['promotionName'].encode('utf-8') == '不参加优惠'
            # 检验活动promotionCode
            assert lst_response2[i]['programLst'][0]['promotion']['promotionCode'] == ""
            # 检验programType(10-->营销活动)
            assert lst_response2[i]['programLst'][0]['programType'] == 0
            # 检验菜品count
            assert lst_response2[i]['programLst'][0]['foodLst'][0]['count'] == lst_price2[i]
            # 检验菜品price
            assert lst_response2[i]['programLst'][0]['foodLst'][0]['count'] == lst_price2[i]
            # 检验菜品名称foodName
            assert lst_response2[i]['programLst'][0]['foodLst'][0]['foodName'].encode('utf-8') == '鱼香肉丝'

    @allure.feature('数据准备:多个特价菜')
    def test_5(self):
        # 删除所有活动
        self.promotionUtils._del_all_promotion_v2()
        # 清除缓存
        self.promotionUtils._clear_info_cache_v2(startDate)
        global lst_bargainprice5, lst_bargainprice52, lst_promotionid5, lst_promotioncode5, lst_price5, lst_price52, lst_response5
        lst_bargainprice5 = [21, 22, 233.2, 23.5, 10.19, 5.0, 66666]
        lst_bargainprice52 = [19, 21, 233.3, 23.7, 6, 3.5, 66668]
        lst_price5 = [21.5, 88.8, 233.3, 23.6, 10.2, 5.1, 66666.6]
        lst_price52 = [21, 21.4, 233.4, 23.8, 10.2, 5.1, 86666.6]
        lst_response5 = []
        lst_promotionid5 = []
        lst_promotioncode5 = []
        for i in range(0, len(lst_price5)):
            # 获取excel中的请求数据
            getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=5, row_id=2)
            # 处理excel中的请求数据
            tmp_result = json.loads(getInputData)
            tmp_result['priceLst'][0]['price'] = lst_bargainprice5[i]
            tmp_result['priceLst'][1]['price'] = lst_bargainprice52[i]
            tmp_result['priceLst'] = json.dumps(tmp_result['priceLst'])
            promotionCode = Module_Pass().get_currentTime2()
            tmp_result['promotionCode'] = promotionCode
            lst_promotioncode5.append(promotionCode)
            # 获取结果
            result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=5, row_id=2, data=tmp_result,
                                                         coo=coo)
            # 从结果中获取响应信息
            result_response = json.loads(result[1][0])
            lst_promotionid5.append(result_response['data']['promotionIDStr'])
            # 从结果中获取excel中期望结果的数据
            result_excel = json.loads(result[0])
            # 进行接口结果断言
            assert result_response['code'] == result_excel['code']

            print "***这是第[" + str(i) + "]条请求sass营销计算接口***"
            # 获取excel中的请求数据
            getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=5, row_id=3)
            # 处理excel中的请求数据
            tmp_result = json.loads(getInputData)
            tmp_result['foodLst'][0]['count'] = str(lst_price5[i])  # 菜品1数量
            tmp_result['foodLst'][0]['price'] = str(lst_price5[i])  # 菜品1价格
            tmp_result['foodLst'][1]['count'] = str(lst_price52[i])  # 菜品2数量
            tmp_result['foodLst'][1]['price'] = str(lst_price52[i])  # 菜品2价格
            # 获取结果
            result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=5, row_id=3, data=tmp_result)
            # 从结果中获取响应信息
            result_response = json.loads(result[1][0])
            lst_response5.append(result_response)
            # 从结果中获取excel中期望结果的数据
            result_excel = json.loads(result[0])
            # 进行接口结果断言
            assert result_response['code'] == result_excel['code']

            # 删除所有活动
            self.promotionUtils._del_all_promotion_v2()
            # 清除缓存
            self.promotionUtils._clear_info_cache_v2(startDate)

    @allure.feature('特价菜计算测试')
    def test_6(self):
        # 校验活动打折的金额
        for i in range(0, len(lst_response5)):
            print "***这是第[" + str(i) + "]条测试.price/count:[" + str(lst_price5[i]) + "],菜品特价为:[" + str(
                lst_bargainprice5[i]) + "]***"
            # 校验折扣的金额(小数位取两位，抹掉其余位)

            promotionAmount = round(
                lst_price5[i] * lst_price5[i] + lst_price52[i] * lst_price52[i] - lst_bargainprice5[i] * lst_price5[i]
                - lst_bargainprice52[i] * lst_price52[i], 2)  # 整数相除为0 ，如果是浮点数除法则执行精确除法。
            origin_promotionAmount = lst_response5[i]['programLst'][0]['promotionAmount']
            assert origin_promotionAmount == promotionAmount
            # 校验实收金额
            receivableAmount = round(lst_bargainprice5[i] * lst_price5[i] + lst_bargainprice52[i] * lst_price52[i],
                                     2)  # float类型,4-3.6后精度丢失得0.39999999
            assert lst_response5[i]['programLst'][0]['receivableAmount'] == receivableAmount
            # 校验未折扣的金额
            assert lst_response5[i]['programLst'][1]['promotionAmount'] == 0
            # 校验未折扣的实收金额
            receivableAmount = round(lst_price5[i] * lst_price5[i] + lst_price52[i] * lst_price52[i], 2)
            assert lst_response5[i]['programLst'][1]['receivableAmount'] == receivableAmount
            # 校验promotionID
            assert lst_response5[i]['programLst'][0]['promotion']['promotionID'] == lst_promotionid5[i]
            # 检验活动类别
            assert lst_response5[i]['programLst'][0]['promotion']['categoryName'].encode('utf-8') == '特价菜angle'
            # 检验活动promotionCode
            assert lst_response5[i]['programLst'][0]['promotion']['promotionCode'] == lst_promotioncode5[i]
            # 检验programType(10-->营销活动)
            assert lst_response5[i]['programLst'][0]['programType'] == 10
            # 检验菜品count
            assert lst_response5[i]['programLst'][0]['foodLst'][0]['count'] == lst_price52[i]
            assert lst_response5[i]['programLst'][0]['foodLst'][1]['count'] == lst_price5[i]
            # 检验菜品price
            assert lst_response5[i]['programLst'][0]['foodLst'][0]['count'] == lst_price52[i]
            assert lst_response5[i]['programLst'][0]['foodLst'][1]['count'] == lst_price5[i]
            # 检验菜品名称foodName
            assert lst_response5[i]['programLst'][0]['foodLst'][0]['foodName'].encode('utf-8') == '酸菜鱼'
            assert lst_response5[i]['programLst'][0]['foodLst'][1]['foodName'].encode('utf-8') == '鱼香肉丝'
