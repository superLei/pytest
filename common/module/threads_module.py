# coding:utf-8
import threading
import multiprocessing


class Threading_Utils():
    def __init__(self):
        """
        初始化类
        """
        self.__threads = []

    def add_thread(self, rev_func, rev_arg=None):
        """
        将线程加入到线程池
        :param rev_func:接收线程函数
        :param args: 线程函数需要传递的参数（参数类型为元组）
        :return:返回线程池
        """
        __thread = threading.Thread(target=rev_func, args=rev_arg)
        self.__threads.append(__thread)
        return self.__threads

    def run_threads(self):
        for __thread in self.__threads:
            __thread.start()
        for __thread in self.__threads:
            __thread.join()


class Multiprocessing_utlis():
    def __init__(self):
        """
        初始化类
        """
        self.__processing = []

    def add_processing(self, rev_func, rev_arg=None):
        """
        将线程加入到线程池
        :param rev_func:接收进程函数
        :param args: 进程函数需要传递的参数（参数类型为元组）
        :return:返回进程池
        """
        __process = multiprocessing.Process(target=rev_func, args=rev_arg)
        self.__processing.append(__process)
        return self.__processing

    def run_processing(self):
        for tmp_process in self.__processing:
            tmp_process.start()
        for tmp_process in self.__processing:
            tmp_process.join()
