# coding=utf-8
# !/usr/bin/env python
# coding=utf-8
from __future__ import print_function
import subprocess
import os
import platform


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


def check_alerts():
    try:
        output = subprocess.check_output(['alias'], stderr=subprocess.STDOUT, shell=True)
        print("Yes----alerts后门")
    except subprocess.CalledProcessError:
        print("No----alerts后门")


def check_sshkey():
    file_path = "/root/.ssh/authorized_keys"
    if os.path.exists(file_path):
        print("Yes----ssh公私密钥后门")
    else:
        print("Yes----ssh公私密钥后门")


def check_adduser():
    root_gid = 0  # GID for "root"
    # Get current user's GID
    current_gid = os.getgid()
    # Check if current user is a member of the root group
    if current_gid == root_gid:
        print("yes----ssh后门用户")
    else:
        print("No----ssh后门用户")


def check_crontab():
    cron_files = ["/etc/crontab"]
    for cron_file in cron_files:
        if os.access(cron_file, os.W_OK):
            print("yes----计划任务后门")
        else:
            print("No----计划任务后门")


def check_strace():
    j = ml('strace -V')
    if 'strace -- version' in j:
        print("yes----strace后门")
    else:
        print("No----strace后门")


def check_ssh_Soft_link():
    command = 'cat /etc/ssh/sshd_config|grep UsePAM'
    j = ml(command)
    if 'UsePAM yes' in j:
        print("yes----SSH软链接后门")
    else:
        print("No----SSH软链接后门")


def check_Rootkit():
    system_info = platform.uname()
    kernel_version = platform.release()
    # 定义支持的最低和最高内核版本
    min_kernel_version = {
        'Centos 6.10': '2.6.32-754.6.3.el6.x86_64',
        'Centos 7': '3.10.0-862.3.2.el7.x86_64',
        'Centos 8': '4.18.0-147.5.1.el8_1.x86_64',
        'Ubuntu 18.04.1 LTS': '4.15.0-38-generic'
    }
    max_kernel_version = {
        'Centos 6.10': '2.6.32',
        'Centos 7': '3.10.0',
        'Centos 8': '4.18.0',
        'Ubuntu 18.04.1 LTS': '4.15.0'
    }
    current_os = system_info[0] + ' ' + system_info[2] + ': ' + kernel_version
    if current_os in min_kernel_version:
        min_version = min_kernel_version[current_os]
        max_version = max_kernel_version[current_os]

        if min_version <= kernel_version <= max_version:
            print("yes----Rootkit后门：https://github.com/f0rb1dd3n/Reptile/")
    else:
        print("No----Rootkit后门")


if __name__ == '__main__':
    print('HackerPermKeeper')
    print('OpenSSH后门太过久远，而且很可能会导致ssh连接报错，所以不建议使用[只测试过乌班图14版本成功]')
    check_adduser()
    check_alerts()
    check_crontab()
    check_ssh_Soft_link()
    check_sshkey()
    check_strace()
    check_Rootkit()
