# coding:utf-8

import hashlib
import setting
#import url_resource
from common.module import restquests_module

log = setting.logging

'''md5加密'''


def md5_module(rev_str):
    __md5_encryption = hashlib.md5()
    __md5_encryption.update(rev_str)
    return __md5_encryption.hexdigest()

'''拼接为sign'''


def get_sign(**_input):
    del _input["sign"]
    lst = []
    for keys, value in _input.items():
        if value is not None:
            temp = keys + value
            lst.append(temp)
    lst.sort()
    result = "".join(lst)
    result += "GHTSKey123!";

    __md5_encryption = hashlib.md5()
    __md5_encryption.update(result.encode('UTF-8'))
    sign = __md5_encryption.hexdigest()
    return sign

'''获得AES加密数据'''


def get_aes_encrypt(key, data):
    __get_resp = restquests_module.Get_Response(url_resource.ENCRYPT_TOOL)
    __data = {'key': key, 'data': data}
    __resp = __get_resp.get_response(params=__data)
    __an_resp = restquests_module.Analysis_Response(__resp)
    __resp = __an_resp.STR_CONTENT
    return __resp


'''获得AES解密参数'''


def get_aes_decrypt(key, data):
    __get_resp = restquests_module.Get_Response(url_resource.DECRYPT_TOOL)
    __data = {'key': key, 'data': data}
    __resp = __get_resp.get_response(params=__data)
    __an_resp = restquests_module.Analysis_Response(__resp)
    __resp = __an_resp.STR_CONTENT
    return __resp


if __name__ == '__main__':
    cid = 300100
    q = 'blablabla'
    aes_key = "qwereqwrwqefsafsdvgf"
    q = get_aes_encrypt(aes_key, q)
    sign = get_sign(**excelDate_input)
    print "--------------工具类测试----------------"
    print q
    print sign
