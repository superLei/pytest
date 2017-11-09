# encoding = utf-8
import setting
from common.module import mysql_module

class DB_Operation:
    def __init__(self):
        pass

    def db_read(self, sqlexp):
        select_rec = mysql_module.Mysql_Module().DataRead(sqlexp)
        return select_rec

    def db_write(self, sqlexp):
        select_rec = mysql_module.Mysql_Module().DataWrite(sqlexp)
        return select_rec


if __name__ == '__main__':
    # print DB_Operation().db_read("select * from tbl_mendian_order_master limit 1")
    print DB_Operation().db_read('select foodAmount ,promotionAmount  from tbl_mendian_order_master where orderKey = "20170726140110760561960176"')
