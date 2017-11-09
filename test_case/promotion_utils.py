# -*- coding: UTF-8 -*-
import sys
import json
import db_excluded
import http_excluded
from setting import ENVIRONMENT_CONFIG
from common.service import excel_case_facade
from common.service.module_pass_facade import Module_Pass
from data import get_current_path



class PromotionUtils:
    def __init__(self):
        self.sheet_index = 1
        _file_name = '/test_saas.xlsx'
        _file_path = get_current_path.get_cur_path()
        self.filename = _file_path + _file_name
        self.excel_facade = excel_case_facade.GetExcelCaseDate()
        self.host = ENVIRONMENT_CONFIG["test"]['queryTransNum']

    # 删除所有营销活动
    def _del_all_promotion(self):
        # 获取结果
        """
        :rtype: object
        """
        result = self.excel_facade.get_case_data_crm(self.filename, self.sheet_index, row_id=6)
        # 从结果中获取响应信息
        result_response = json.loads(result[1][0])
        # 从结果中获取excel中期望结果的数据
        result_excel = json.loads(result[0])
        # 进行接口结果断言
        if result_response['code'] == result_excel['code'] and result_response['message'] == result_excel['message']:
            return True
        else:
            return False

    # 删除所有营销活动
    def _del_all_promotion_v2(self):
        # 获取结果
        """
        :rtype: object
        """
        url = self.host + '/test/event/specifiedGroup?groupID=11009'
        result = self.excel_facade.get_case_data_act2(url, 'delete', '')
        # 进行接口结果断言
        if json.loads(result)['code'] == "000" and json.loads(result)['message'] == "000":
            print '***成功删除营销活动***'
            return True
        else:
            print '***删除营销活动失败***'
            return False

    # 添加营销活动
    # def _add_promotion(self, num):
    #     n = num
    #     while n > 0:
    #         # 获取excel中的请求数据
    #         getInputData = self.excel_facade.get_case_input(self.filename, self.sheet_index, row_id=2)
    #         # 处理excel中的请求数据
    #         tmp_result = json.loads(getInputData)
    #         tmp_result['ruleJson'] = json.dumps(tmp_result['ruleJson'])
    #         tmp_result['timeLst'] = json.dumps(tmp_result['timeLst'])
    #         tmp_result['priceLst'] = json.dumps(tmp_result['priceLst'])
    #         tmp_result['scopeLst'] = json.dumps(tmp_result['scopeLst'])
    #         promotionCode = Module_Pass().get_currentTime2()
    #         tmp_result['promotionCode'] = promotionCode
    #         # 获取结果
    #         result = self.excel_facade.get_case_data_crm(self.filename, self.sheet_index, row_id=2, data=tmp_result,
    #                                                      coo=self._login())
    #         # 从结果中获取响应信息
    #         result_response = json.loads(result[1][0])
    #         # 从结果中获取excel中期望结果的数据
    #         result_excel = json.loads(result[0])
    #         # 进行接口结果断言
    #         if result_response['code'] == result_excel['code']:
    #             continue
    #         n = n - 1

    # 登录系统
    def _login(self):
        result = self.excel_facade.get_case_data_crm(self.filename, self.sheet_index, 1)
        act_result_login = json.loads(result[1][0])
        except_result_login = json.loads(result[0])
        # 进行结果断言
        if act_result_login['code'] == except_result_login['code']:
            # 保存cookie
            coo = 'access_token=' + result[1][1]['access_token']
        else:
            coo = 'login failed'
        return coo

    # 清除缓存
    def _clear_info_cache(self, orderdate):
        isOk = False
        url = self.host +'/test/infocache/clear.ajax?groupID=11009&orderDate=' + orderdate
        result = self.excel_facade.get_case_data_act2(url,'get','')

        if json.loads(result)['code'] == 0:
            print '***成功清除缓存***'
            isOk = True
        else:
            print '***清除缓存失败***'
            print result
        return isOk

    # 清除缓存v2
    def _clear_info_cache_v2(self, orderdate):
        isOk = False
        url = self.host +'/test/infocache/clear.ajax?groupID=11009&orderDate=' + orderdate
        result = self.excel_facade.get_case_data_act2(url,'get','')

        if json.loads(result)['code'] == 0:
            print '***成功清除缓存***'
            isOk = True
        else:
            print '***清除缓存失败***'
            print result
        return isOk

    '''master数据表比较'''
    def _db_master_compare(self,d_db,d_http):
        # d_http = {}
        # d_db = {}
        lst_excluded = ['cityLst','orgIDLst','excludedShopIDLst','consumeTimeLst','submitTimeLst','crmLevelLst','crmConditionsJson','foodScopeType','categoryCodeLst','foodCodeLst','excludedFoodNameLst',
               'sharedPromotionIDLst','roleIDLst','maintenanceLevel','maintenanceOrgID','modifiedBy','script']
        for i in range(0,len(lst_excluded)):
            d_db.pop(lst_excluded[i])
        if cmp(d_db,d_http) == 0:
            return True
        else:
            return False

    '''food_price表比较'''
    def _db_foodprice_compare(self,d_db,d_http):
        lst_excluded = ['actionStamp','createStamp','action']
        for i in range(0, len(lst_excluded)):
            print lst_excluded[i]
            d_db.pop(lst_excluded[i])
        if cmp(d_db, d_http) == 0:
            return True
        else:
            return False

    '''和数据库表比较数据'''
    def _db_compare_http(self, d_db, d_http,table_name,http_name):
        lst_excluded = db_excluded.MYSQL_TABLE[table_name]
        lst_excluded2 = http_excluded.ADD_NEW[http_name]
        for i in range(0,len(lst_excluded)):
            d_db.pop(lst_excluded[i])
        for j in range(0,len(lst_excluded2)):
            d_http.pop(lst_excluded2[j])
        print 'db\'s result:'
        print d_db
        print 'http\'s result:'
        print d_http
        for d in d_http:
            re = cmp(d_db[d], d_http[d])
            if re == 0:
                return True
            elif re == 1:
                print 'd_db > d_http'
                return False
            else:
                print 'd_db < d_http'
                return False

    '''和数据库表比较数据'''
    def _db_compare_http_v2(self, d_db, d_http):
        print 'db\'s result:'
        print d_db
        print 'http\'s result:'
        print d_http
        for d in d_http:
            re = cmp(d_db[d], d_http[d])
            if re == 0:
                return True
            elif re == 1:
                print 'd_db > d_http'
                return False
            else:
                print 'd_db < d_http'
                return False


    '''解析json'''
    def _json_to_math(self, dict_origin):
        foodLst = dict_origin['programLst'][0]['foodLst']
        foodLst_count = len(foodLst)
        price_count = 0
        price_total = 0
        for i in range(0,foodLst_count):
            price_count += foodLst[i]['count']
            price_total += foodLst[i]['count'] * foodLst[i]['payPrice']
        price_count = round(price_count,2)
        price_total = round(price_total,2)
        return price_count, price_total, foodLst_count

    '''
    添加活动
    '''
    def _add_promotions(self,dict_rulejson,sheet_index,row,coo):
        # 获取excel中的请求数据
        getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=sheet_index, row_id=row)
        # 处理excel中的请求数据
        dict1_input = json.loads(getInputData)
        tmp_result = json.loads(getInputData)
        if dict_rulejson is not None and dict_rulejson != {} :
            for i in dict_rulejson.keys():
                tmp_result[i] = dict_rulejson[i]
        tmp_result['scopeLst'] = json.dumps(tmp_result['scopeLst'])
        tmp_result['priceLst'] = json.dumps(tmp_result['priceLst'])
        tmp_result['ruleJson'] = json.dumps(tmp_result['ruleJson'])
        promotionCode = Module_Pass().get_currentTime2()
        tmp_result['promotionCode'] = promotionCode
        # 获取结果
        result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=sheet_index, row_id=row,
                                                     data=tmp_result,
                                                     coo=coo)
        # 从结果中获取响应信息
        result_response = json.loads(result[1][0])
        promotionid = result_response['data']['promotionIDStr']
        # 从结果中获取excel中期望结果的数据
        result_excel = json.loads(result[0])
        # 进行接口结果断言
        assert result_response['code'] == result_excel['code']
        return promotionid, promotionCode,dict1_input

    '''请求sass营销计算接口'''
    def _execute_promotions(self,dict_dishinfo,sheet_index,row):
        # 获取excel中的请求数据
        getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=sheet_index, row_id=row)
        # 处理excel中的请求数据
        tmp_result = json.loads(getInputData)
        if dict_dishinfo is not None and dict_dishinfo != {}:
            for i in dict_dishinfo.keys():
                tmp_result['foodLst'][0][i] = dict_dishinfo[i]
        # dict2_input = tmp_result
        # 获取结果
        result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=sheet_index, row_id=row,
                                                     data=tmp_result)
        # 从结果中获取响应信息
        result_response = json.loads(result[1][0])
        # 从结果中获取excel中期望结果的数据
        result_excel = json.loads(result[0])
        # 进行接口结果断言
        assert result_response['code'] == result_excel['code']
        return result_response,tmp_result,result_excel

    '''请求sass营销计算接口'''

    def _execute_promotions_v2(self, dict_dishinfo, sheet_index, row):
        # 获取excel中的请求数据
        getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=sheet_index, row_id=row)
        # 处理excel中的请求数据
        tmp_result = json.loads(getInputData)
        if dict_dishinfo is not None and dict_dishinfo != {}:
            for i in dict_dishinfo.keys():
                tmp_result[i] = dict_dishinfo[i]
        # 获取结果
        result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=sheet_index, row_id=row,
                                                     data=tmp_result)
        # 从结果中获取响应信息
        result_response = json.loads(result[1][0])
        # 从结果中获取excel中期望结果的数据
        result_excel = json.loads(result[0])
        # 进行接口结果断言
        assert result_response['code'] == result_excel['code']
        return result_response, tmp_result, result_excel

    '''
    活动编辑接口
    tmp_result中必须要有promotionID，promotionCode
    '''
    def _edit_promotions(self,dict_json,sheet_index,row,coo):
        # 获取excel中的请求数据
        getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=sheet_index, row_id=row)
        # 处理excel中的请求数据
        dict1_input = json.loads(getInputData)
        tmp_result = json.loads(getInputData)
        if dict_json is not None and dict_json != {}:
            for i in dict_json.keys():
                tmp_result[i] = dict_json[i]
        tmp_result['scopeLst'] = json.dumps(tmp_result['scopeLst'])
        tmp_result['priceLst'] = json.dumps(tmp_result['priceLst'])
        tmp_result['ruleJson'] = json.dumps(tmp_result['ruleJson'])

        # 获取结果
        result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=sheet_index, row_id=row,
                                                     data=tmp_result,
                                                     coo=coo)
        # 从结果中获取响应信息
        result_response = json.loads(result[1][0])
        # promotionid = result_response['data']['promotionIDStr']
        # 从结果中获取excel中期望结果的数据
        result_excel = json.loads(result[0])
        # 进行接口结果断言
        assert result_response['code'] == result_excel['code']
        return dict1_input

    '''
    启用和禁用活动
    '''
    def _enable_promotions(self,dict_json,sheet_index,row,coo):
        # 获取excel中的请求数据
        getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=sheet_index, row_id=row)
        # 处理excel中的请求数据
        tmp_result = json.loads(getInputData)
        if dict_json is not None and dict_json != {}:
            for i in dict_json.keys():
                tmp_result[i] = dict_json[i]
        # tmp_result['ruleJson'] = json.dumps(tmp_result['ruleJson'])
        # 获取结果
        result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=sheet_index, row_id=row,
                                                     data=tmp_result,
                                                     coo=coo)
        # 从结果中获取响应信息
        result_response = json.loads(result[1][0])
        # 从结果中获取excel中期望结果的数据
        result_excel = json.loads(result[0])
        # 进行接口结果断言
        assert result_response['code'] == result_excel['code']
        return tmp_result,result_response

    '''
    detail接口获取活动详情
    '''
    def _detail_promotions(self,dict_json,sheet_index,row,coo):
        # 获取excel中的请求数据
        getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=sheet_index, row_id=row)
        # 处理excel中的请求数据
        tmp_result = json.loads(getInputData)
        if dict_json is not None and dict_json != {}:
            for i in dict_json.keys():
                tmp_result[i] = dict_json[i]
        # 获取结果
        result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=sheet_index, row_id=row,
                                                     data=tmp_result,
                                                     coo=coo)
        # 从结果中获取响应信息
        result_response = json.loads(result[1][0])
        # 从结果中获取excel中期望结果的数据
        result_excel = json.loads(result[0])
        # 进行接口结果断言
        assert result_response['code'] == result_excel['code']
        return tmp_result,result_response

    '''
    查询卡参与活动的次数
    '''
    def _queryTransNum(self,dict_json,sheet_index,row):
        # 获取excel中的请求数据
        getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=sheet_index, row_id=row)
        # 处理excel中的请求数据
        tmp_result = json.loads(getInputData)
        if dict_json is not None and dict_json != {}:
            for i in dict_json.keys():
                tmp_result[i] = dict_json[i]
        # 获取结果
        result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=sheet_index, row_id=row,
                                                     data=tmp_result)
        # 从结果中获取响应信息
        result_response = json.loads(result[1][0])
        # 从结果中获取excel中期望结果的数据
        result_excel = json.loads(result[0])
        # 进行接口结果断言
        assert result_response['code'] == result_excel['code']
        return tmp_result, result_response

    def _publicMethod(self,dict_json,sheet_index,row):
        # 获取excel中的请求数据
        getInputData = self.excel_facade.get_case_input(self.filename, sheet_index=sheet_index, row_id=row)
        # 处理excel中的请求数据
        tmp_result = json.loads(getInputData)
        if dict_json is not None and dict_json != {}:
            for i in dict_json.keys():
                tmp_result[i] = dict_json[i]
        # 获取结果
        result = self.excel_facade.get_case_data_crm(self.filename, sheet_index=sheet_index, row_id=row,
                                                     data=tmp_result)
        # 从结果中获取响应信息
        result_response = json.loads(result[1][0])
        # 从结果中获取excel中期望结果的数据
        result_excel = json.loads(result[0])
        # 进行接口结果断言
        assert result_response['code'] == result_excel['code']
        return tmp_result, result_response

    '''基础营销发劵'''
    def _giftItem(self,dict_json,sheet_index,row):
        return self._publicMethod(dict_json,sheet_index,row)

    '''123'''
    def test(self,dict_rulejson):
        tmp_result1 = json.dumps({"ruleJson":{"giftValue":"100","points":"1","targetScope":"0","voucherVerify":"0","costIncome":"1","evidence":"0","stageType":"2","giftPrice":"1","voucherVerifyChannel":"1","blackList":1,"stage":[{"stageAmount":"1","giftMaxUseNum":1}],"transFee":"0"}})
        tmp_result = json.loads(tmp_result1)
        if dict_rulejson is not None:
            for i in dict_rulejson.keys():
                tmp_result[i] = dict_rulejson[i]
        return tmp_result


if __name__ == '__main__':
    util = PromotionUtils()
    dict_rulejson = {"giftPrice":"0"}
    print util.test(dict_rulejson)
    dict1 = {}
    print dict1 is None
    # util.test(dict_rulejson)
