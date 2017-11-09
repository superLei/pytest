# coding:utf-8
import datetime
from common.module import unittest_module

'''
Biz层封装工具类
'''


class SuiteReporter_Utils():
    def __init__(self):
        pass

    def __make_report_file_name(self, test_module):
        """
        报告命名规范及定义
        :param test_module: 被测模块，字符串
        :return:返回报告名
        """
        __date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-')
        __report_file_name = "../report/" + __date + test_module + ".html"
        return __report_file_name

    def run_and_report(self, test_module, report_file_name, title, description, verbosity=1):
        """
        运行和生成报告
        :param test_module:测试模块
        :param report_file_name: 报告名
        :param title: 报告标题
        :param description: 报告描述
        :param verbosity: 报告级别，默认为1
        :return:
        """
        __suite_list = []
        __unittest_utils = unittest_module.Unittest_Module()
        for tmp in test_module:
            __test_suite = __unittest_utils.load_case_from_module(tmp)
            __suite_list.append(__test_suite)
        __total_suite = __unittest_utils.make_suite(__suite_list)
        __report_file_name = self.__make_report_file_name(report_file_name)
        __stream = file(__report_file_name, "wb")
        __unittest_utils.run_suite(__total_suite, report=True, stream=__stream, title=title, description=description,
                                   verbosity=verbosity)

# if __name__ == '__main__':
#     Business_Utils().case_assert("../data/test_case_saas.xlsx", sheet_index=0, id=2)
