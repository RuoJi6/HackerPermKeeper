# -*- coding: utf-8 -*-
# !/usr/bin/env python

from __future__ import print_function
import subprocess
import os, sys
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


def get_files_in_current_directory():
    current_directory = '/root/.ssh/'
    try:
        files = os.listdir(current_directory)

        file_names = []
        for file in files:
            if os.path.isfile(os.path.join(current_directory, file)):
                file_names.append(file)

        return file_names
    except Exception as e:
        return 'No'


def check_sshkey():
    user = ml('whoami').strip()
    if 'root' in user:
        file_path = "/root/.ssh/authorized_keys"
        if os.path.exists(file_path):
            print("Yes----ssh公私密钥后门")
        else:
            print("Yes----ssh公私密钥后门")
    else:
        file_path = "/home/" + user + "/.ssh/authorized_keys"
        if os.path.exists(file_path):
            print("Yes----ssh公私密钥后门")
        else:
            print("Yes----ssh公私密钥后门")
    if os.access('/etc/ssh/sshd_config', os.W_OK):
        # （例如 os.R_OK 表示可读，os.W_OK 表示可写，os.X_OK 表示可执行）
        print('      可以修改sshd_config配置文件')
    else:
        print('      没有权限修改sshd_config文件')


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
    user = ml('whoami').strip()
    user = '/var/spool/cron/' + user
    cron_files = ["/etc/crontab", user, '/var/spool/cron/crontabs']
    print('计划任务后门')
    for cron_file in cron_files:
        if os.access(cron_file, os.W_OK):
            print('  ' + cron_file + '---yes')


def check_strace():
    j = ml('strace -V')
    if 'strace -- version' in j:
        print("yes----strace后门")
    else:
        print("No----strace后门")


def check_ssh_Soft_link():
    j = ml('cat /etc/ssh/sshd_config|grep UsePAM')
    j1 = ml('whoami').strip()
    if 'UsePAM yes' in j and 'root' in j1:
        print("yes----SSH软链接后门")
        return 1
    else:
        print("No----SSH软链接后门[如果是root权限，可以直接SSH软链接模块运行开启]")
        return 0


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


def check_python():
    try:
        j = ml('python3 -V')
        if 'Python 3' in j:
            print("yes----python3")
        else:
            print("No----python")
        # 检查 Python 2
        output = subprocess.Popen(['python2', '-V'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        if 'Python 2' in output[1].decode():
            print("yes----python2")
            return
    except OSError:
        pass


def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除" + script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)


def ssh_Soft_link_cromtab():
    user = ml('whoami').strip()
    user = '/var/spool/cron/' + user
    cron_files = ["/etc/crontab", user, '/var/spool/cron/crontabs']
    print('计划任务&ssh软链接后门')
    for cron_file in cron_files:
        if os.access(cron_file, os.W_OK):
            print('  ' + cron_file + '---yes')

def ssh_cromtab_ssh_key():
    user = ml('whoami').strip()
    user = '/var/spool/cron/' + user
    cron_files = ["/etc/crontab", user, '/var/spool/cron/crontabs','/etc/ssh/sshd_config']
    print('计划任务&sshkey后门')
    for cron_file in cron_files:
        if os.access(cron_file, os.W_OK):# （例如 os.R_OK 表示可读，os.W_OK 表示可写，os.X_OK 表示可执行）
            print('  ' + cron_file + '---yes')


def check_user():
    user = ml('id').strip()
    print('权限为' + str(user))


if __name__ == '__main__':
    print('HackerPermKeeper v2.0')
    print('OpenSSH后门太过久远，而且很可能会导致ssh连接报错，所以不建议使用[只测试过乌班图14版本成功]')
    check_adduser()
    check_alerts()
    check_crontab()
    check_ssh_Soft_link()
    check_sshkey()
    check_strace()
    check_Rootkit()
    check_python()
    ssh_Soft_link_cromtab()
    ssh_cromtab_ssh_key()
    check_user()
    delete_current_script()  # 删除当前执行脚本文件
