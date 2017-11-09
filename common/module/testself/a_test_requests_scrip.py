# coding:utf-8
import unittest

import setting
from common.module import restquests_module

log = setting.logging


class test(unittest.TestCase):
    def setUp(self):
        self.se = restquests_module.Get_Response('get').with_session
        print "setup"

    def tearDown(self):
        print "teardown"

    def test001(self):
        print "test001"

    def test002(self):
        print 'test002'

    def test003(self):
        print 'test003'
        assert False

    def test004(self):
        print 'test004'

    def runTest(self):
        pass

#
# from python_utils import unittest_utils
# ut = unittest_utils.Unittest_Utils()
# ut.add_case_to_suite(testself('test001'))
# ut.add_case_to_suite(testself('test001'))
# namelist = ut.get_testcase_names(testself('test001'))
# e = ut.load_case_from_testclass(testself)
# f = ut.load_case_from_names(['test_requests_utils'])
# g = ut.load_case_from_name('test_requests_utils')
# h = ut.load_case_from_module('test_requests_utils')
# # ut1 = unittest_utils.Unittest_Utils()
# # b = ut1.add_case_to_suite(testself('test001'))
# # ut1.add_case_to_suite(testself('test002'))
# # ut1.add_cases_to_suite(a)
# # c=ut1.add_suite_to_suite(a)
# ut.add_suite_to_suite(e)
# ut.add_cases_to_suite(e)
# ut.run_suite()
# unittest.TextTestRunner().run(f)
