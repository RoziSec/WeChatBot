#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : read_config.py
# @Author : Norah C.IV
# @Time : 2022/9/30 0:11
# @Software: PyCharm
import os
import configparser  # 引入模块

config = configparser.ConfigParser()  # 实例化一个对象
config_path = os.path.dirname(os.path.abspath(__file__)) + "/config.ini"
config.read(config_path, encoding='utf-8')


class ReadConfig:
    @staticmethod
    def from_dict(keys, values):
        value = config.get(keys, values)
        return value
