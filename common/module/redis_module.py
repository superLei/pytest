# coding:utf-8
import redis

"""
:param
:return
"""


class CallRedis:
    def __init__(self):
        pass

    def get_redis_data(self):
        dic = {'6379': 0, '6380': 0, '6381': 0, '6382': 0}
        for key in dic:
            # print key
            r = redis.StrictRedis(host='192.168.88.88', port=key)
            # r.set("zpz", "info")
            # print r.keys("xxx:x:xxx*")
            dic[key] = r.keys("xxx:x:xxx*")
            print dic[key]
            print dic['6380']
            if dic[key] is '[]':
                ret = 'redis is empty...'
                return ret
        return True


if __name__ == '__main__':
    print CallRedis().get_redis_data()
