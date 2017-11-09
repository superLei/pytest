# -*- coding: UTF-8 -*-
import setting

__aurhor__ = "zpz"

import MySQLdb
from common.module.env_module import Env_Module


class DB_Operation:
    def __init__(self):
        self.env = Env_Module().get_env_url()

    def DataSelect(self, sqlpara):
        if self.env == setting.ENVIRONMENT_CONFIG["dohko"]:
            conn = MySQLdb.connect(setting.MYSQL_CONFIG["dohko"])
            cur = conn.cursor()
            sql = sqlpara
            cur.execute(sql)
            rows = cur.fetchall()
            cur.close()
            return rows
        else:
            print "DB Permission Rufused!"

    def DataUpdateOrDelete(self, sqlpara, envInput=None):
        if self.env == setting.ENVIRONMENT_CONFIG["dohko"]:
            conn = MySQLdb.connect(setting.MYSQL_CONFIG["dohko"])
            cur = conn.cursor()
            sql = sqlpara
            cur.execute(sql)
            conn.commit()
            cur.close()
        else:
            print "DB Permission Rufused!"


if __name__ == '__main__':
    print DB_Operation().DataSelect("SELECT * FROM * where * = *")
    # print DB_Operation().DataUpdate("UPDATE * SET * = 2 where id =100")
