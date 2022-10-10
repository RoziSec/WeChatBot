#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : Bot.py
# @Author : Norah C.IV
# @Time : 2022/9/29 15:21
# @Software: PyCharm
from PyOfficeRobot.core.WeChatType import *
from config.read_config import ReadConfig
from lib.dbSQLite import DBTool
from lib.log import logger

db = DBTool()
title = '[每日POC推送]'
interval = '|'


class WeChatBot(object):
    @staticmethod
    def Pusher():
        wx = WeChat()
        wx.GetSessionList()

        msg, uuid_list = WeChatBot.Data()
        msg = msg[0:-1]
        who = ReadConfig().from_dict('customer', 'name')

        wx.ChatWith(who)
        wx.SendMsg(msg)

        WeChatBot.Update(uuid_list)

    @staticmethod
    def Data():
        query_poc_ob = []
        query_poc = "select * from exploit where pushed is 0 limit 10"
        result = db.executeQuery(query_poc, query_poc_ob)

        info = title + interval
        uuid_list = []
        for data in result.fetchall():
            if data is not None:
                # data[0]为uuid值、data[1]为利用类型、data[2]为漏洞名称、data[3]为POC链接
                msg = '---------------' + interval + data[2] + interval + '[URL] ' + data[3] + interval
                info = info + msg
                uuid_list.append(data[0])
            else:
                break

        return info, uuid_list

    @staticmethod
    def Update(uuid_list):
        for uuid in uuid_list:
            update_exploit_ob = [(uuid,)]
            update_exploit = 'update exploit set pushed = 1 where id = ?'
            db.executeUpdate(update_exploit, update_exploit_ob)
            logger.info("Exploit's uuid {} is updated.".format(uuid))
        db.close()


if __name__ == '__main__':
    WeChatBot.Pusher()
