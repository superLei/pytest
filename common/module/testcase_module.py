# coding:utf-8
import unittest
import types


class MyTestCase(unittest.TestCase):

    def runTest(self):
        self._testFunc()

    def assertEqual(self, first, second, msg=None):
        if type(second) is types.UnicodeType:
            print "Actual:"
            print first.encode('utf-8')
            print "Expect:"
            print second.encode('utf-8')
        else:
            print "Actual:"
            print first
            print "Expect:"
            print second

        assertion_func = self._getAssertEqualityFunc(first, second)
        assertion_func(first, second, msg=msg)




