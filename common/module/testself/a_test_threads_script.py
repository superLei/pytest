# coding:utf-8
import time


def a(str):
    print time.ctime()
    print str


from common.module import threads_module

th_utils = threads_module.Threading_Utils()
for i in range(100):
    th_utils.add_thread(a, rev_arg=(i,))
th_utils.run_threads()
