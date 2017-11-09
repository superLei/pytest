# coding:utf-8

import requests
from requests.exceptions import *
import logging


# from requests.auth import HTTPBasicAuth, HTTPDigestAuth, HTTPProxyAuth, AuthBase


class Get_Response(object):
    def __init__(self, rev_url, rev_method='get'):
        """
        初始化类，接收被测url,获取response方法（默认 get 方法）
        """
        self.__url = rev_url
        self.__method = rev_method.lower()
        self.with_session = requests.session()

    def get_response(self, session=False, *args, **kwargs):
        """
        获取response
        session : 为True则启用session进行请求,默认不带session
        可接参数
        params : 需要传递的参数
        stream : 设置为True可以获取raw的response，并且只能获取headers信息，直到访问content属性
        headers : 指定头信息
        data : 传递参数为表单，使用data参数
        timeout : 设置超时
        auth : 身份认证
        cookies : cookies
        allow_redirects : 是否支持重定向
        proxies : 设置代理
        verify : 设置是否忽略https 主机ssl证书，默认为True (仅用于主机证书)
        cert : 指定本地证书为客户端证书 是一个元组，元组里可以接多个本地证书的路径
        files : 上传的文件
        hooks : 钩子，可以传递一些事件，在获取response的时候
        """
        if self.__method == 'get' and session == False:
            try:
                __resp = requests.get(self.__url, *args, **kwargs)
            except (MissingSchema, InvalidURL):
                logging.error('请检查url = %s 的正确性' % self.__url)
            except ConnectionError:
                logging.error('请检查网络连接情况与api响应时间')
            else:
                return __resp
        elif self.__method == 'get' and session == True:
            try:
                __resp = self.with_session.get(self.__url, *args, **kwargs)
            except (MissingSchema, InvalidURL):
                logging.error('请检查url = %s 的正确性' % self.__url)
            except ConnectionError:
                logging.error('请检查网络连接情况与api响应时间')
            else:
                return __resp

        elif self.__method == 'post' and session == False:
            try:
                __resp = requests.post(self.__url, *args, **kwargs)
            except (MissingSchema, InvalidURL):
                logging.error('请检查url = %s 的正确性' % self.__url)
            except ConnectionError:
                logging.error('请检查网络连接情况与api响应时间')
            else:
                return __resp
        elif self.__method == 'post' and session == True:
            try:
                __resp = self.with_session.post(self.__url, *args, **kwargs)
            except (MissingSchema, InvalidURL):
                logging.error('请检查url = %s 的正确性' % self.__url)
            except ConnectionError:
                logging.error('请检查网络连接情况与api响应时间')
            else:
                return __resp
        elif self.__method == 'put':
            try:
                __resp = requests.put(self.__url, *args, **kwargs)
            except (MissingSchema, InvalidURL):
                logging.error('请检查url = %s 的正确性' % self.__url)
            except ConnectionError:
                logging.error('请检查网络连接情况与api响应时间')
            else:
                return __resp
        elif self.__method == 'delete':
            try:
                __resp = requests.delete(self.__url, **kwargs)
                return __resp
            except:
                logging.error('请检查url = %s 的正确性' % self.__url)
        elif self.__method == 'head':
            try:
                __resp = requests.head(self.__url, **kwargs)
            except (MissingSchema, InvalidURL):
                logging.error('请检查url = %s 的正确性' % self.__url)
            except ConnectionError:
                logging.error('请检查网络连接情况与api响应时间')
            else:
                return __resp
        elif self.__method == 'options':
            try:
                __resp = requests.options(self.__url, **kwargs)
            except (MissingSchema, InvalidURL):
                logging.error('请检查url = %s 的正确性' % self.__url)
            except ConnectionError:
                logging.error('请检查网络连接情况与api响应时间')
            else:
                return __resp
        else:
            logging.error('请检查method = %s 的正确性' % self.__method)


class Analysis_Response:
    """
    解析response
    """

    def __init__(self, rev_resp):
        """
        初始化类
        :param rev_resp:接收response
        """
        self.__resp = rev_resp

    @property
    def URL(self):
        """
        获取url
        :return:返回url
        """
        __url = self.__resp.url
        return __url

    @property
    def STATUS_CODE(self):
        """
        获取状态吗
        :return:返回状态码
        """
        __status_code = self.__resp.status_code
        return __status_code

    @property
    def HEADERS(self):
        """
        获取响应头
        :return:返回响应头
        """
        __headers = self.__resp.headers
        return __headers

    @property
    def STR_CONTENT(self):
        """
        以str形式获取相应内容
        :return:返回str的content
        """
        __str_response = self.__resp.content
        return __str_response

    @property
    def DIC_CONTENT(self):
        """
        将response转换为字典返回
        :return:返回字典格式的response
        """
        __dic_content = self.__resp.json()
        return __dic_content

    @property
    def COOKIES(self):
        __cookies = self.__resp.cookies
        return __cookies
