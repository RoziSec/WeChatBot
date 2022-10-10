#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : main.py
# @Author : Norah C.IV
# @Time : 2022/10/11 0:48
# @Software: PyCharm
from function.exploit import Exploit
from function.Bot import WeChatBot


def main():
    print("\033[0;32m[+] Starting get Exploit!\033[0m")
    Exploit.get_exp()
    print("\033[0;32m[+] Running WeChatBot!\033[0m")
    WeChatBot.Pusher()
    print("\033[0;31m[+] Task Finished!\033[0m")


if __name__ == '__main__':
    print('''
    ______           __      _ __  ____        __ 
   / ____/  ______  / /___  (_) /_/ __ )____  / /_
  / __/ | |/_/ __ \/ / __ \/ / __/ __  / __ \/ __/
 / /____>  </ /_/ / / /_/ / / /_/ /_/ / /_/ / /_  
/_____/_/|_/ .___/_/\____/_/\__/_____/\____/\__/  
          /_/                                     
                    友情提示：搭配searchsploit使用
                    Powered by Norah C.IV''')
    main()
