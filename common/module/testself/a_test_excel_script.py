# coding:utf-8
import sys

from common.module import excel_module

sys.path.append("..")
import unittest


class Test_Excel_Utils(unittest.TestCase):
    file_name = ''

    def setUp(self):
        self.utils = excel_module.Read_Excel('../../data/test_case_saas.xlsx')
        self.sheet = self.utils.get_sheet_by_index(0)

    def tearDown(self):
        pass

    def test_get_sheet_by_index(self):
        __table = self.utils.get_sheet_by_index(0)
        print __table

    def test_get_sheet_by_name(self):
        __table = self.utils.get_sheet_by_name(u"表1")
        print __table

    def test_get_row_values(self):
        __sheet = self.utils.get_sheet_by_index(0)
        row_values_list = self.utils.get_row_values(__sheet, 0)
        print row_values_list

    def test_get_col_values(self):
        __sheet = self.utils.get_sheet_by_index(0)
        col_values_list = self.utils.get_col_values(__sheet, 0)
        print col_values_list

    def test_get_number_of_rows(self):
        rows_num = self.utils.get_number_of_rows(self.sheet)
        print rows_num

    def test_get_number_of_cols(self):
        cols_num = self.utils.get_number_of_cols(self.sheet)
        print cols_num

    def test_get_cell_value(self):
        cell_value = self.utils.get_cell_value(self.sheet, 0, 0)
        print cell_value

    def test_get_all_content(self):
        content = self.utils.get_all_content(self.sheet)
        print content
        self.assertEqual('编号', content[0][0])
