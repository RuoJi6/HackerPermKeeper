# coding=utf-8
# !/usr/bin/env python
from __future__ import print_function  # python2 3输出打印
import subprocess  # 执行命令
import sys, os


def ml(command):
    # 调用用于启动一个子进程来执行命令。command 变量应该包含您要执行的命令。shell=True 参数告诉 subprocess 使用shell来解释命令。
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()  # 等待子进程完成

    stdout, stderr = process.communicate()  # 用于获取子进程的标准输出和错误输出。这个方法返回一个元组，包含子进程的标准输出和标准错误输出。
    try:
        decoded_stdout = stdout.decode('utf-8')
    except UnicodeDecodeError:
        decoded_stdout = stdout.decode('latin1')
    try:
        decoded_stderr = stderr.decode('utf-8')
    except UnicodeDecodeError:
        decoded_stderr = stderr.decode('latin1')
    return decoded_stdout  # 用于获取子进程的标准输出和错误输出。这个方法返回一个元组，包含子进程的标准输出和标准错误输出。


def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除" + script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)


if __name__ == '__main__':
    match = "3"  # 删除 .bash_history后面match几行
    ml("sed -i '" + match + ",$d' .bash_history")
    ml('set +o history')  # 当前用户不记录历史命令
    print('已经删除.bash_history文件中 {' + match + '} 行')
    print('当前用户不记录历史命令，请执行{ history -c }刷新{重启失效}')
    delete_current_script()
