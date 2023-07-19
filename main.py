# coding=utf-8
# !/usr/bin/env python


from colorama import init
from termcolor import colored
from argparse import ArgumentParser
import os
import sys

from config import configs
from config import configss
from choose import chooses

init()


try:
    name = colored('HackerPermKeeper v1.0 by 弱鸡 https://github.com/ytMuCheng/HackerPermKeeper/', 'green')
    arg = ArgumentParser(description=name )  # 创建解析器, description内容就是
    arg.add_argument("-m", "--multiple", help="选择权限维持模块 -m 1")
    arg.add_argument("-c", "--config", help="查看支持的权限维持模块 -c 1,查看详细使用说明 -c 2 ")
    args = arg.parse_args()  # 解析参数
    multiple = args.multiple  # 接受参数
    config = args.config  # 接受参数
    if multiple != None or config != None:
        if multiple != None:
            chooses()
        if config != None:
            if config == '1':
                configss()
            elif config == '2':
                configs()
            else:
                print('输入错误')
                configss()

    else:
        os.system('python main.py -h')
        sys.exit()

except KeyboardInterrupt as error:  # ctr +c
    print(colored(f'\n------------------------------------------', 'red'), '{', colored("程序终止", "green"), '}',
          colored(f'------------------------------------------', 'red'))
    sys.exit()
