# coding=utf-8
# !/usr/bin/env python
from __future__ import print_function

import os
import subprocess
import sys


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


def miyue(new_content, filename):  # /etc/environment   cen /etc/profile
    with open(filename, 'a') as file:
        file.write(new_content + '\n')


def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除" + script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)


if __name__ == '__main__':
    j = ml('cat /etc/os-release')
    if 'ubuntu' in j:
        print('ubuntu')
        miyue('HISTCONTROL=ignorespace', '/etc/environment')
        ml('source  /etc/environment')
    elif 'centos' in j:
        print('centos')
        miyue('HISTCONTROL=ignorespace', '/etc/profile')
        ml('source  /etc/profile')
    ml('history -c')
    print('请输入命令进行测试: [空格]命令  输出指定历史命令[history -d id]')
    print('请执行{ history -c }刷新情况当前用户bash')
    delete_current_script()  # 删除当前执行脚本文件
