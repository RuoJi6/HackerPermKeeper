# coding=utf-8
# !/usr/bin/env python

from __future__ import print_function
from colorama import init
from termcolor import colored
from argparse import ArgumentParser
import os
import sys

from config import configs
from config import configss
from choose import chooses
import subprocess

init()

try:
    name_data = 'HackerPermKeeper[黑客权限保持者] 项目地址: https://github.com/RuoJi6/HackerPermKeeper'
    lod = colored("""
      _    _            _             _____                    _  __                         
     | |  | |          | |           |  __ \                  | |/ /                         
     | |__| | __ _  ___| | _____ _ __| |__) |__ _ __ _ __ ___ | ' / ___  ___ _ __   ___ _ __ 
     |  __  |/ _` |/ __| |/ / _ \ '__|  ___/ _ \ '__| '_ ` _ \|  < / _ \/ _ \ '_ \ / _ \ '__|
     | |  | | (_| | (__|   <  __/ |  | |  |  __/ |  | | | | | | . \  __/  __/ |_) |  __/ |   
     |_|  |_|\__,_|\___|_|\_\___|_|  |_|   \___|_|  |_| |_| |_|_|\_\___|\___| .__/ \___|_|   
                                                                            | |              
                                                                            |_|                                             
    """, 'magenta')
    print(
        lod + colored(
            "                                                                                     v6.0 by:弱鸡",
            'blue')
    )
    arg = ArgumentParser(description=colored(name_data, 'cyan'))  # 创建解析器, description内容就是
    arg.add_argument("-m", "--multiple", help="选择权限维持模块 -m 1")
    arg.add_argument("-c", "--config", help="查看支持的权限维持模块 -c 1,查看详细使用说明 -c 2 ")
    args = arg.parse_args()  # 解析参数
    multiple = args.multiple  # 接受参数
    config = args.config  # 接受参数
    if multiple != None or config != None:
        if multiple != None:
            chooses(name_data)
        if config != None:
            if config == '1':
                configss(name_data)
            elif config == '2':
                configs(name_data)
            else:
                print('输入错误')
                configss(name_data)

    else:
        print(colored(f'\n-------------------------', 'red'), '{',
              colored("请使用python3运行，或者输入main.py --help 查看帮助", "green"), '}',
              colored(f'-------------------------', 'red'))
        sys.exit()

except KeyboardInterrupt as error:  # ctr +c
    print(colored(f'\n------------------------------------------', 'red'),
          '{', colored("程序退出", "green"), '}',
          colored(f'------------------------------------------', 'red')
          )
    sys.exit()
