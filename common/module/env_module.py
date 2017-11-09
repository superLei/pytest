# coding:utf-8

import logging
import sys
from setting import ENVIRONMENT_CONFIG
from setting import MYSQL_CONFIG


class Env_Module():
    def __init__(self):
        """
        初始化
        """
        pass

    def get_env_url(self, env):
        """
        :return:返回命令行环境映射地址
        """
        env_url = ENVIRONMENT_CONFIG["test"]
        # env_url = ENVIRONMENT_CONFIG["dohko"]
        # if sheet_index in (0, 1, 2, 3):
        return env_url[env]

    def get_env_mysql_para(self, env):
        """返回mysql参数"""
        env_mysql = MYSQL_CONFIG[env]
        return env_mysql


