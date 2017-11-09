# coding:utf-8
import unittest

import setting
from common.module import xml_module

log = setting.logging


class Test_Xml_Utils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.xml_utils = xml_module.Xml_Utils_For_File("../../data/test_xml_utils.xml")
        cls.xml_str = '''<?xml version="1.0" encoding="utf-8"?>
                            <catalog>
                                <maxid>4</maxid>
                                <login username="pytest" passwd='123456'>
                                    <caption>Python</caption>
                                    <item id="4">
                                        <caption>测试</caption>
                                    </item>
                                </login>
                                <login username="pytest" passwd='123456'>
                                    <caption>Python</caption>
                                    <item id="4">
                                        <caption>测试</caption>
                                    </item>
                                </login>
                                <item id="2">
                                    <caption>Zope</caption>
                                </item>
                            </catalog>'''
        cls.xml_utils2 = xml_module.Xml_Utils_For_Str(cls.xml_str)

    def setUp(self):
        self.root = self.xml_utils.root
        __ele_list = self.xml_utils.find_elements_by_tag_name('item')
        self.__ele = __ele_list[0]

        self.root2 = self.xml_utils2.root
        log.debug(self.root2)

    def test_get_elements_by_tagname(self):
        self.xml_utils.find_elements_by_tag_name('caption')

    def test_get_child_nodes(self):
        __nodes_list = self.xml_utils.find_child_nodes(self.__ele)

    def test_get_ele_data(self):
        self.xml_utils.get_ele_data([])

    def test_get_ele_attribute(self):
        self.xml_utils.get_ele_attribute(self.__ele, 'id')

    def test_get_node_name(self):
        self.xml_utils.get_node_name(self.__ele)

    def test_find_all_child_nodes(self):
        list = self.xml_utils2.find_all_child_nodes(self.root2, 'login')
        log.debug(list)
        for i in list:
            text = self.xml_utils2.find_first_child_node(i, 'caption').text
            log.debug(text)
