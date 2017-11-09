# coding:utf-8

import unittest
import logging
from common.integretion import HTMLTestRunner


class Unittest_Module:
    def __init__(self):
        self.suite = self.make_suite()
        self.__loader = unittest.TestLoader()

    def make_suite(self, rev_suite=None):
        if rev_suite is None:
            rev_suite = []
        self.__suite = unittest.TestSuite(rev_suite)
        logging.info('测试套件已建立')
        return self.__suite

    def add_case_to_suite(self, rev_case):
        """
        添加测试用例到测试套件套件
        :param rev_case:接收测试用例  格式：class('case')
        :return:测试套件
        """
        self.suite.addTest(rev_case)
        logging.debug('测试套件 %s' % self.suite)
        return self.suite

    def add_cases_to_suite(self, rev_cases):
        """
        添加测试用例到测试套件套件
        :param rev_case:接收测试用例,也可以是一个测试套件  格式：[class('case001'),class('case002')]
        :return:返回测试套件
        """
        self.suite.addTests(rev_cases)
        logging.debug('测试套件 %s' % self.suite)
        return self.suite

    def add_suite_to_suite(self, rev_suite):
        """
        :param rev_suite:如果加入一个测试套件可以直接传入，多个测试套件以元组的形式传入
        :return:返回测试套件
        """
        __suite = self.make_suite(rev_suite)
        logging.debug('测试套件 %s' % __suite)
        return __suite

    def get_testcase_names(self, rev_test_class):
        __name_list = unittest.TestLoader().getTestCaseNames(rev_test_class)
        logging.debug('%s 类获取到的用例名称：%s ' % (rev_test_class, __name_list))
        return __name_list

    def load_case_from_module(self, rev_module):
        """
        一个模块的实例来获取测试用例，模块必须包含runTest()方法
        :param rev_module:模块的实例
        :return:返回测试套件
        """
        __suite = self.__loader.loadTestsFromModule(rev_module)
        logging.debug('测试套件 %s' % __suite)
        return __suite

    def load_case_from_testclass(self, rev_class):
        """
        通过类名来获取测试用例，
        :param rev_class: 接收测试类
        :return:返回测试套件
        """
        __suite = self.__loader.loadTestsFromTestCase(rev_class)
        logging.debug('测试套件 %s' % __suite)
        return __suite

    def load_case_from_names(self, rev_names):
        """
        从模块里面读取测试用例
        :param rev_names: 接收模块名，类型为列表
        :return:返回测试套件
        """
        __suite = self.__loader.loadTestsFromNames(rev_names)
        logging.debug('测试套件 %s' % __suite)
        return __suite

    def load_case_from_name(self, rev_name):
        """
        从模块里面读取测试用例
        :param rev_names: 接收模块名，类型为字符串
        :return:返回测试套件
        """
        __suite = self.__loader.loadTestsFromName(rev_name)
        logging.debug('测试套件 %s' % __suite)
        return __suite

    def run_suite(self, rev_suite, report=False, stream='', verbosity=1, title=None, description=None):
        """
        运行测试套件
        :param rev_suite:
        :param description:
        :param title:
        :param verbosity:
        :param stream:
        :param report:是否需要生成报告（默认不带报告）
        :return:
        """
        logging.info('开始执行测试套件')
        if report == False:
            unittest.TextTestRunner().run(rev_suite)
        else:
            runner = HTMLTestRunner.HTMLTestRunner(stream=stream, verbosity=verbosity, title=title,
                                                   description=description)
            runner.run(rev_suite)
        logging.info('测试套件执行结束')
