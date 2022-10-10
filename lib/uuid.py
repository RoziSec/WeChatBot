#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : uuid.py
# @Author : Norah C.IV
# @Time : 2022/8/11 15:19
# @Software: PyCharm
import random
import string

TEXT = string.ascii_letters + string.digits


class RandomId:
    @staticmethod
    def random_id():
        s1 = ''.join(random.sample(TEXT, k=32))
        return s1


if __name__ == '__main__':
    uuid = RandomId.random_id()
    print(uuid)
