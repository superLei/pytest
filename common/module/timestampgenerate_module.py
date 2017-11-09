# coding:utf-8

import time,calendar,datetime

def TinmeStampGenerator():
    """demo 2017149819718718794"""
    timestamp = str(int(time.time()))
    return timestamp

def SystemCurrentTime():
    """获取系统当前时间"""
    now_date = time.strftime('%Y%m%d', time.localtime(time.time()))
    return now_date

def SystemAgoTime():
    """系统180天前日期"""
    now = time.time()
    before = now -180 * 24 * 3600  # 可以改变n 的值计算n天前的
    beforedate = time.strftime("%Y%m%d", time.localtime(before))
    return beforedate

def SystemYesterdayTime():
    """系统当前时间昨天日期"""
    now = time.time()
    before = now -1 * 24 * 3600  # 可以改变n 的值计算n天前的
    beforedate = time.strftime("%Y%m%d", time.localtime(before))
    return beforedate

def SystemTomorrowTime():
    """系统当前时间昨天日期"""
    now = time.time()
    before = now +1 * 24 * 3600  # 可以改变n 的值计算n天前的
    beforedate = time.strftime("%Y%m%d", time.localtime(before))
    return beforedate

def SystemAgoTimebyMin(n):
    """获取n小时前日期，返回时分数值"""
    now = time.time()
    before = now - n* 3600  # 可以改变n 的值计算n小时前的
    beforedate = time.strftime("%H%M", time.localtime(before))#只返回时 分数值
    return beforedate

def SystemAfterTimebyMin(n):
    """获取n小时后日期，返回时分数值"""
    now = time.time()
    after = now + n* 3600  # 可以改变n 的值计算n个小时后的
    afterdate = time.strftime("%H%M", time.localtime(after))#只返回时 分数值
    return afterdate


if __name__ == '__main__':
    # print TinmeStampGenerator()
    print SystemTomorrowTime()
    # print SystemAgoTime()
