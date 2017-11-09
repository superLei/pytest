# coding:utf-8
import json

import MySQLdb
import sys

import setting

log = setting.logging


class Mysql_Module:
    def __init__(self):
        """
        初始化类，定义数据库连接，定义游标
        """
        self.con = ''
        self.cur = ''

    def create_connect(self, dictRet=True, **kwargs):
        """
        初始化类，创建数据库连接，创建游标
        """
        try:
            print kwargs
            self.con = MySQLdb.connect(**kwargs)
            log.info('数据库连接正常，已创建连接')
        except Exception, e:
            log.error('请检查数据的参数是否正确')
            log.error(e)
        else:
            if dictRet == True:
                self.cur = self.con.cursor(cursorclass=MySQLdb.cursors.DictCursor)
                log.info('已创建字典游标')
            else:
                self.cur = self.con.cursor()
                log.info('已创建游标')
            u'''调试代码'''
            # self.cur.execute("select * from tbl_mendian_order_master limit 1")
            # return self.cur.fetchall()
            # self.close_db()

    def DataRead(self, sqlexp, mysql_conf_item):
        """
        获取数据库信息
        :param sqlexp:接收sql语句
        :param search_num: 接收查询条数，与search_all参数互斥
        :param search_all: 是否查询全部，与search_num参数互斥
        :return:返回查询结果
        """
        try:
            # self.create_connect(**json.loads(setting.MYSQL_CONFIG[sys.argv[1]]))
            self.create_connect(**setting.MYSQL_CONFIG[mysql_conf_item])
            self.cur.execute(sqlexp)
        except Exception, e:
            log.error('请检查sql语句 = %s 是否正确' % sqlexp)
        else:
            # log.info(self.cur.fetchall())
            return self.cur.fetchall()
        self.close_db()

    def DataWrite(self, sqlexp, mysql_conf_item):
        u'''delete'''
        # self.create_connect(**json.loads(setting.MYSQL_CONFIG[sys.argv[1]]))
        try:
            self.create_connect(**setting.MYSQL_CONFIG[mysql_conf_item])
            self.cur.execute(sqlexp)
            self.con.commit()
        except:
            self.con.rollback()
            log.info('更新数据失败')
        self.close_db()

    def close_db(self):
        """
        关闭游标，关闭数据库连接
        """
        self.cur.close()
        self.con.close()
        log.info('游标与数据库连接已关闭')


if __name__ == '__main__':
    module = Mysql_Module()
    print module.DataRead('SELECT * FROM `tbl_crm_consumption_detail` WHERE groupID = 11009','dohko')
    sql_add = 'INSERT INTO tbl_crm_consumption_detail (transID, groupID, cardID, transShopID, consumptionAmount, consumptionCanPointAmount, deductionMoneyAmount, giveBalancePay, deductionPointMoneyAmount, deductionGiftAmount, posOrderNo, actionStamp, createStamp)VALUES(1233211234568, 11009, 1233211234567, 12345678,4000, 0, 3766.54,233.46,0,0,9743822932528577,"2017-11-06 11:00:00","2017-11-06 11:00:00");'
    sql_del = 'DELETE FROM `tbl_crm_consumption_detail` WHERE groupID = 11009'
    print module.DataWrite(sql_del,'dohko')
