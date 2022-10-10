#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : setup.py
# @Author : Norah C.IV
# @Time : 2022/9/30 0:13
# @Software: PyCharm
import os
import configparser


config = configparser.ConfigParser()
config_path = os.path.dirname(os.path.abspath(__file__)) + "/config/config.ini"


class WeChatBot:
    @staticmethod
    def init():
        print("[+] Begin to execute initialization of WeChatBot.")
        WeChatBot.create_configurations()
        WeChatBot.create_sqlite_db()
        print("[+] All initialization done.")

    @staticmethod
    def create_configurations():
        print("[+] Creating configurations.")
        config['sqlite'] = {
            'path': os.path.dirname(os.path.abspath(__file__)) + '\\database\\rss.db',
        }

        config['exploit'] = {
            'url': 'https://www.exploit-db.com/rss.xml',
        }

        config['customer'] = {
            'name': '文件传输助手'
        }

        with open(config_path, 'w', encoding='utf-8') as configfile:
            config.write(configfile)
        print("[+] Configurations file '{}' is created.".format(config_path))

    @staticmethod
    def create_sqlite_db():
        import sqlite3

        from config.read_config import ReadConfig

        db_file = ReadConfig().from_dict('sqlite', 'path')
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.executescript('drop table if exists exploit')
        print("[+] Connection '{}' successfully.".format(db_file))

        create_exploit_db = '''
        create table exploit
        (id char primary key not null,
        method char,
        poc_name char,
        url char, 
        pushed int)
        '''

        cursor.execute(create_exploit_db)


if __name__ == '__main__':
    WeChatBot.init()
