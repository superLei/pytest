# coding:utf-8
import random
import time
import uuid

def OrderIdGenerator():
    """demo 2017149819718718794"""
    orderid = "2017" + str(int(time.time())) + str(random.randint(0, 100000))
    return orderid

def UUidGenerator():
    return str(uuid.uuid4())

if __name__ == '__main__':
    print OrderIdGenerator()
    print UUidGenerator()
