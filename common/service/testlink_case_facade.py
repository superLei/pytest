# coding=utf-8

import json
import logging
import sys

import setting

sys.path.append("../")
from common.integretion import testlink_module
from common.module import restquests_module
from common.module import env_module


class GetTestlinkCaseDate:
    def __init__(self):
        self.url = ''
        self.method = ''
        self.data_res = ''
        self.exp_resp = ''
        self.data = ''

    def get_case_data(self, case_name='test'):
        try:
            self.ret = testlink_module.TestLink_Module().get_case(case_name)
        except Exception, e:
            logging.error("------------调用testlink出错！------------")
            print e
        self.data = json.loads(self.ret[0])["data"]
        self.url = env_module.Env_Module().get_env_url() + json.loads(self.ret[0])["path"]
        self.method = json.loads(self.ret[0])["method"]
        """期望返回值获取"""
        exp_resp = self.ret[1]
        logging.info("------------期望值是：------------" + json.dumps(exp_resp))
        print exp_resp
        # # data = "a=%s" % json.dumps({"b": "c"})
        """真实返回值获取"""
        headers = setting.REQUEST_HEADER
        act_resp_handle = restquests_module.Get_Response(self.url, rev_method=self.method)
        act_resp = act_resp_handle.get_response(data=self.data, headers=headers).text
        logging.info("------------真实值是：------------" + json.dumps(act_resp))
        print act_resp
        # resp_analysis = restquests_module.Analysis_Response(act_resp)
        # act_resp_dic = resp_analysis.DIC_CONTENT
        # self.assertIn(expect, act_resp, "notmatch")
        return exp_resp, act_resp


if __name__ == '__main__':
    GetTestlinkCaseDate().get_case_data("test")
