# coding:utf-8

import hashlib
import json
import logging
from setting import ENVIRONMENT_CONFIG
from common.module import restquests_module


def unicode_to_utf(dict):
    __dict = {}
    for key, value in dict.items():
        try:
            key = key.encode("utf-8")
            value = value.encode("utf-8")
            __dict[key] = value
        except:
            __dict[key] = value
    return __dict


# md5加密
def md5_utils(rev_str):
    __md5_encryption = hashlib.md5()
    __md5_encryption.update(rev_str)
    return __md5_encryption.hexdigest()


# 拼接为sign
def get_sign(cid=None, q=None, uid='', aes_key=''):
    __sign_str = "cid=%s;q=%s%s%s" % (cid, q, uid, aes_key)
    __get_resp = restquests_module.Get_Response(url_resource.MD5_TOOL)
    __data = {'data': __sign_str}
    logging.info(__data)
    __resp = __get_resp.get_response(params=__data)
    __an_resp = restquests_module.Analysis_Response(__resp)
    __resp = __an_resp.STR_CONTENT
    return __resp


# 获得AES加密数据
def get_aes_encrypt(key, data):
    __get_resp = restquests_module.Get_Response(url_resource.ENCRYPT_TOOL)
    __data = {'key': key, 'data': data}
    __resp = __get_resp.get_response(params=__data)
    __an_resp = restquests_module.Analysis_Response(__resp)
    __resp = __an_resp.STR_CONTENT
    return __resp


# 获得AES解密参数
def get_aes_decrypt(key, data):
    __get_resp = restquests_module.Get_Response(url_resource.DECRYPT_TOOL)
    __data = {'key': key, 'data': data}
    __resp = __get_resp.get_response(params=__data)
    __an_resp = restquests_module.Analysis_Response(__resp)
    __resp = __an_resp.STR_CONTENT
    logging.debug("json格式的response = %s" % __resp)
    __resp = json.loads(__resp)
    # __resp = unicode_to_utf(__resp)
    return __resp


if __name__ == '__main__':
    cid = 300100
    q = '{"channelType":2,"cityName":"赤峰市","vehicleModelId":27131,' \
        '"vehiclePrice":"80000","registDate":"2015-01-01","purchaseTaxIsLoaned":0,' \
        '"purchaseTax": 0,"processType":2,"discountAmt":0}'

    print q
    aes_key = "qwereqwrwqefsafsdvgf"
    q = get_aes_encrypt(aes_key, q)

    sign = get_sign(cid=300100, q=q, aes_key=aes_key)
    print "##################"
    print q
    print sign
