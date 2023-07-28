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


def ml(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()  # 等待子进程完成

    stdout, stderr = process.communicate()  # 获取子进程的输出和错误
    try:
        decoded_stdout = stdout.decode('utf-8')
    except UnicodeDecodeError:
        decoded_stdout = stdout.decode('latin1')
    try:
        decoded_stderr = stderr.decode('utf-8')
    except UnicodeDecodeError:
        decoded_stderr = stderr.decode('latin1')
    return decoded_stdout


# def check_python():
#     j = ml('python -V')
#     j2 = ml('python2 -V')
#     j3 = ml('python3 -V')
#     if 'Python 3' in j or 'Python 3' in j3:
#         print("py3")
#     elif 'Python 2' in j2 or 'Python 2' in j3:
#         print("py2")
#     else:
#         print('No')

try:
    name = colored('HackerPermKeeper v2.0 by 弱鸡 https://github.com/RuoJi6/HackerPermKeeper', 'green')
    arg = ArgumentParser(description=name)  # 创建解析器, description内容就是
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
        print(colored(f'\n-------------------------', 'red'), '{', colored("请使用python3运行，或者输入main.py --help 查看帮助", "green"), '}',
              colored(f'-------------------------', 'red'))
        sys.exit()

except KeyboardInterrupt as error:  # ctr +c
    print(colored(f'\n------------------------------------------', 'red'), '{', colored("程序终止", "green"), '}',
          colored(f'------------------------------------------', 'red'))
    sys.exit()
