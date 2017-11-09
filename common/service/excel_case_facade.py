# -*- coding: UTF-8 -*-

import json
import logging
import setting
import requests
import copy
from common.module import env_module
from common.module import excel_module
from common.module import restquests_module
from common.service import module_pass_facade

import sys

sys.path.append("..")


class GetExcelCaseDate:
    """
    初始化获取excelData
    1、获取对应id的行的内容
    2、获取url
    3、获取请求方式
    4、获取请求参数，并进行转码
    5、获取预期结果
    6、将预期结果转换为字典
    7、设置headers
    8、获取response
    9、获取字典格式的response
    :param file_name: 测试数据的文件名
    :param sheet_index: sheet表的索引
    :param id: caseId
    :return:
    """

    def __init__(self):
        self.url = ''
        self.method = ''
        self.data_res = ''
        self.exp_resp = ''
        self.data = ''
        self.case_url = ''
        self.case_input = ''

    def get_case_data_crm(self, file_name, sheet_index=0, row_id=0, data=None, **kwargs):
        # type: (object, object, object, object, object) -> object
        """
        1、获取对应id的行的内容
        2、获取url
        3、获取请求方式
        4、获取请求参数，并进行转码
        5、获取预期结果
        8、获取string类型response
        :param file_name: 测试数据的文件名
        :param sheet_index: sheet表的索引
        :param id: caseId
        :return:exp_resp_dic,act_resp_dic
        """
        excel_handle = excel_module.Read_Excel(file_name)
        sheet = excel_handle.get_sheet_by_index(sheet_index)
        case_data_list = excel_handle.get_row_values(sheet, row_id)
        path = case_data_list[1]
        self.url = self.get_url(path)
        # self.url = env_module.Env_Module().get_env_url(sheet_index) + path
        self.method = case_data_list[2]
        self.data_res = case_data_list[3]
        self.exp_resp = case_data_list[4]
        self.contype = json.loads(case_data_list[5])
        self.data = json.loads(self.data_res, encoding="utf-8")
        logging.info(self.data_res)
        if kwargs is not None:
            for i in kwargs:
                for j in self.data:
                    if i == j:
                        self.data[j] = kwargs[i]
        if data is not None:
            self.data = data
        exp_resp = self.get_case_data_exp()
        access_token = ''
        for i in kwargs:
            if i == 'coo':
               access_token = kwargs[i]
        print "\n" + "Url:"
        print self.url.encode('utf-8')
        if(access_token.strip()==''):
            act_resp = self.get_case_data_act_crm()
        else:
            act_resp = self.get_case_data_act_crm(access_token=access_token)
        # print "\n" + "Input"
        # print self.data_res.encode('utf-8')
        print("\n" + "exp_resp:" + "\n" + exp_resp + "\n\n" + "act_resp:" + "\n" + act_resp[0] + "\n")
        return exp_resp, act_resp

    def get_case_data_crm2(self, file_name, sheet_index=0, row_id=0, data=None, **kwargs):
        # type: (object, object, object, object, object) -> object
        """
        1、获取对应id的行的内容
        2、获取url
        3、获取请求方式
        4、获取请求参数，并进行转码
        5、获取预期结果
        8、获取string类型response
        :param file_name: 测试数据的文件名
        :param sheet_index: sheet表的索引
        :param id: caseId
        :return:exp_resp_dic,act_resp_dic
        """
        excel_handle = excel_module.Read_Excel(file_name)
        sheet = excel_handle.get_sheet_by_index(sheet_index)
        case_data_list = excel_handle.get_row_values(sheet, row_id)
        path = case_data_list[1]
        self.url = self.get_url(path)
        # self.url = env_module.Env_Module().get_env_url(sheet_index) + path
        self.method = case_data_list[2]
        self.data_res = case_data_list[3]
        self.exp_resp = case_data_list[4]
        self.contype = json.loads(case_data_list[5])
        self.data = json.loads(self.data_res, encoding="utf-8")
        logging.info(self.data_res)
        if kwargs is not None:
            for i in kwargs:
                for j in self.data:
                    if i == j:
                        self.data[j] = kwargs[i]
        if data is not None:
            self.data = data
        exp_resp = self.get_case_data_exp()
        access_token = ''
        for i in kwargs:
            if i == 'coo':
                access_token = kwargs[i]

        if (access_token.strip() == ''):
            act_resp = self.get_case_data_act_crm()
        else:
            act_resp = self.get_case_data_act_crm(access_token=access_token)
        print "\n" + "Url:"
        print self.url.encode('utf-8')
        print "\n" + "Input"
        print self.data_res.encode('utf-8')
        print("\n" + "exp_resp:" + "\n" + exp_resp + "\n\n" + "act_resp:" + "\n" + act_resp[0] + "\n")
        return exp_resp, act_resp

    def get_case_data(self, file_name, sheet_index=0, row_id=0, data=None, **kwargs):
        """
        1、获取对应id的行的内容
        2、获取url
        3、获取请求方式
        4、获取请求参数，并进行转码
        5、获取预期结果
        8、获取string类型response
        :param file_name: 测试数据的文件名
        :param sheet_index: sheet表的索引
        :param id: caseId
        :return:exp_resp_dic,act_resp_dic
        """
        excel_handle = excel_module.Read_Excel(file_name)
        sheet = excel_handle.get_sheet_by_index(sheet_index)
        case_data_list = excel_handle.get_row_values(sheet, row_id)
        path = case_data_list[1]
        # self.url = env_module.Env_Module().get_env_url(sheet_index) + path
        self.get_url(path)
        self.method = case_data_list[2]
        self.data_res = case_data_list[3]
        self.exp_resp = case_data_list[4]
        self.data = json.loads(self.data_res, encoding="utf-8")
        logging.info(self.data_res)
        if kwargs is not None:
            for i in kwargs:
                for j in self.data:
                    if i == j:
                        self.data[j] = kwargs[i]
        if data is not None:
            self.data = data
        exp_resp = self.get_case_data_exp()
        act_resp = self.get_case_data_act()
        case_url = self.url
        case_input = case_data_list[3]
        print "\n" + "Url:"
        print case_url.encode('utf-8')
        print "\n" + "Input"
        print case_input.encode('utf-8')
        print("\n" + "exp_resp:" + "\n" + exp_resp + "\n\n" + "act_resp:" + "\n" + act_resp + "\n")
        return exp_resp, act_resp

    def get_case_input(self, file_name, sheet_index=0, row_id=0):
        """
        真实数据获取
        1、获取实际结果
        2、获取真实结果
        :return:exp_resp_dic,act_resp_dic
        """
        excel_handle = excel_module.Read_Excel(file_name)
        sheet = excel_handle.get_sheet_by_index(sheet_index)
        case_data_list = excel_handle.get_row_values(sheet, row_id)
        self.data = case_data_list[3]
        return self.data

    def get_case_input_url(self, file_name, sheet_index=0, row_id=0):
        """
        真实数据获取
        1、获取实际结果
        2、获取真实结果
        :return:exp_resp_dic,act_resp_dic
        """
        excel_handle = excel_module.Read_Excel(file_name)
        sheet = excel_handle.get_sheet_by_index(sheet_index)
        case_data_list = excel_handle.get_row_values(sheet, row_id)
        self.data = case_data_list[1]
        return self.data

    def get_url(self, path):
        pathStr = str(path)
        if pathStr.startswith(r"/login"):
            self.url = env_module.Env_Module().get_env_url('login') + path
            return self.url
        elif pathStr.startswith(r"/api"):
            self.url = env_module.Env_Module().get_env_url('crm') + path
            return self.url
        elif pathStr.startswith(r"/test/event/specifiedGroup"):
            self.url = env_module.Env_Module().get_env_url('delgroup') + path
            return self.url
        elif pathStr.startswith(r"/test/promotion/getShopPromotionByDate.ajax"):
            self.url = env_module.Env_Module().get_env_url('getShopPromotionByDate') + path
            return self.url
        elif pathStr.startswith(r"/test/promotionv2/execute.ajax"):
            self.url = env_module.Env_Module().get_env_url('promotion_v2') + path
            return self.url
        elif pathStr.startswith(r"/test/promotionv2/queryTransNum.ajax"):
            self.url = env_module.Env_Module().get_env_url('queryTransNum') + path
            return self.url
        elif pathStr.startswith(r"/test/promotionv2/sendVoucher.ajax"):
            self.url = env_module.Env_Module().get_env_url('queryTransNum') + path
            return self.url

    def get_case_data_exp(self):
        """
        预期结果获取
        1、直接获取预期结果
        2、将预期结果转换为字典
        :return:预期结果
        """
        logging.debug("-----------------1.expect-------------------------" + self.exp_resp)
        return self.exp_resp.encode("utf-8")

    def get_case_data_act(self):
        """
        真实数据获取
        1、设置headers
        2、获取response
        3、获取字典格式的response
        :return:实际结果
        """
        headers = copy.copy(setting.REQUEST_HEADER)
        act_resp_handle = restquests_module.Get_Response(self.url, rev_method=self.method)
        act_resp_cur = act_resp_handle.get_response(data=self.data, headers=headers)
        resp_analysis = restquests_module.Analysis_Response(act_resp_cur)
        act_resp = resp_analysis.STR_CONTENT
        logging.debug("-----------------data---------------------------" + json.dumps(self.data))
        logging.debug("-----------------headers---------------------------" + json.dumps(headers))
        logging.debug("-----------------2.real-------------------------" + act_resp)
        return act_resp

    def get_case_data_act2(self,url,method,data):
        """
        真实数据获取
        1、设置headers
        2、获取response
        3、获取字典格式的response
        :return:实际结果
        """
        headers = copy.copy(setting.REQUEST_HEADER)
        act_resp_handle = restquests_module.Get_Response(url, method)
        act_resp_cur = act_resp_handle.get_response(data=data, headers=headers)
        resp_analysis = restquests_module.Analysis_Response(act_resp_cur)
        act_resp = resp_analysis.STR_CONTENT
        print "\n" + "Input"
        print json.dumps(self.data)
        logging.debug("-----------------data---------------------------" + json.dumps(self.data))
        logging.debug("-----------------headers---------------------------" + json.dumps(headers))
        logging.debug("-----------------2.real-------------------------" + act_resp)
        return act_resp

    def get_case_data_act_crm(self, **kwargs):
        """
        真实数据获取
        1、设置headers
        2、获取response
        3、获取字典格式的response
        :return:实际结果
        """
        headers = copy.copy(setting.REQUEST_HEADER)
        headers['content-type'] = self.contype['content-type']
        for i in kwargs:
            if i == "access_token":
                headers['Cookie'] =kwargs[i]
        act_resp_handle = restquests_module.Get_Response(self.url, rev_method=self.method)
        if(headers['content-type']=='application/json'):
            act_resp_cur = act_resp_handle.get_response(data=json.dumps(self.data), headers=headers)
        else:
            act_resp_cur = act_resp_handle.get_response(data= self.data, headers=headers)
        # act_resp_cur = act_resp_handle.get_response(data=self.data, headers=headers)
        resp_analysis = restquests_module.Analysis_Response(act_resp_cur)
        act_resp = resp_analysis.STR_CONTENT
        cookies = requests.utils.dict_from_cookiejar(resp_analysis.COOKIES)
        print "\n" + "Input"
        print json.dumps(self.data)
        logging.debug("-----------------data---------------------------" + json.dumps(self.data))
        logging.debug("-----------------2.real-------------------------" + act_resp)
        return act_resp, cookies


    # def exp_resp_edit(self, file_name, sheet_index=0, row_id=0, **kwargs):
    #     excel_handle = excel_module.Read_Excel(file_name)
    #     sheet = excel_handle.get_sheet_by_index(sheet_index)
    #     case_data_list = excel_handle.get_row_values(sheet, row_id)
    #     self.exp_resp = case_data_list[4]
    #     if kwargs is not None:
    #         for i in kwargs:
    #             if i == 'exp_resp':
    #
    #         exp_resp_edit = exp_resp_origin
    #     return exp_resp_edit

