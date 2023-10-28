# coding=utf-8
# !/usr/bin/env python

from __future__ import print_function
from colorama import init
from termcolor import colored


init()


def configs(name_data):
    print(colored(name_data, 'green'))
    print(colored('1--------------OpenSSH后门', 'yellow'),colored('[利用]', 'red'))
    print('OpenSSH后门  优点：直接重置目标服务器的OpenSSH，在里面写入万能密码以及记录ssh明文账户代码 ''  缺点：需要依大量的依赖环境，而且只能使用低版本系统，目前经过测试的有乌班图14',colored('[建议指数：*]\n', 'red'))

    print(colored('2--------------后门用户', 'yellow'),colored('[利用]', 'red'))
    print('后门用户  优点：直接写入后门用户，而且不生成home目录下文件,快捷方便,所有系统支持   缺点：容易发现',colored('[**]\n', 'red'))

    print(colored('3--------------Alias别名后门', 'yellow'),colored('[利用]', 'red'))
    print('Alias别名后门  优点：使用别名来执行命令或者反弹shell,如执行ls,设置之后,就会反弹shell   缺点：需要当前用户执行命令为常用命令',colored('[***]\n', 'red'))

    print(colored('4--------------crontab计划任务', 'yellow'),colored('[利用]', 'red'))
    print('crontab计划任务  优点：设置计划任务来执行反弹shell,其中参考了挖矿病毒计划任务，其中有直接执行crontab来写入，还有直接写入/etc/crontab文件中   缺点：出网执行反弹shell，在流量会被发现',colored('[****]\n', 'red'))

    print(colored('5--------------ssh软连接后门', 'yellow'),colored('[利用]', 'red'))
    print('ssh软连接后门  优点：快速设置ssh连接，不需要密码   缺点：在流量会被发现',colored('[****]\n', 'red'))

    print(colored('6--------------ssh公私密钥后门', 'yellow'),colored('[利用]', 'red'))
    print('ssh公私密钥后门  优点：快速设置密钥连接，其中参考了挖矿病毒ssh公私密钥，管理员很难发现   缺点：在流量会被发现', colored('[*****]\n', 'red'))

    print(colored('7--------------Strace后门', 'yellow'),colored('[利用]', 'red'))
    print('Strace后门  优点：键盘记录的后门,记录ssh明文以及密钥   缺点：需要配合权限维持使用',colored('[****]\n', 'red'))

    print(colored('8--------------Rootkit后门', 'yellow'),colored('[检测]', 'blue'))
    print('Rootkit后[使用的是github项目]  优点：很难发现，几乎不可能发现，而且Rootkit后门包括了反弹shell[使用netstat -tulnp，不会显示]，文件隐藏等   缺点：对于系统版本要求很严格',colored('[****]', 'red'))
    print('项目地址：https://github.com/f0rb1dd3n/Reptile/\n')

    print(colored('9--------------不记录命令[history]', 'yellow'), colored('[利用]', 'blue'))
    print('不记录命令[history]  优点：命令前加空格不记录命令   缺点：需要在命令前加空格',colored('[******]\n', 'red'))

    print(colored('10--------------ssh软链接&crontab', 'yellow'), colored('[利用]', 'blue'))
    print('快速生成软链接[需要运行脚本成功后，一分钟连接]，并且执行计划任务，每分钟判断当前软链接是否存在，如果被kill掉，就重新执行',colored('[*****]\n', 'red'))

    print(colored('11--------------sshkey密钥&crontab', 'yellow'), colored('[利用]', 'blue'))
    print('判断文件是否存在，判断文件是否加锁，判断文件内容是否符合，每分钟检查一次，不存在的话就重新生成执行',colored('[*****]\n', 'red'))

    print(colored('12--------------php权限维持不死免杀马', 'yellow'), colored('[利用]', 'red'))
    print('利用ignore_user_abort函数一直生成文件，同时修改连接命令，加密连接命令',colored('[*****]\n', 'red'))

    print(colored('13--------------check检查脚本', 'yellow'), colored('[利用]', 'red'))
    print('快速检测目标机器可以使用那个权限维持模块，并且检测当前机器处于docker还是k8s，并检测docker逃逸', colored('[*****]', 'red'))

def configss(name_data):
    print(colored(name_data, 'green'))
    print(colored('1--------------OpenSSH后门', 'yellow'),colored('[利用]', 'red'))
    print(colored('2--------------后门用户', 'yellow'),colored('[利用]', 'red'))
    print(colored('3--------------Alias后门', 'yellow'),colored('[利用]', 'red'))
    print(colored('4--------------crontab计划任务', 'yellow'),colored('[利用]', 'red'))
    print(colored('5--------------ssh软连接后门', 'yellow'),colored('[利用]', 'red'))
    print(colored('6--------------ssh公私密钥后门', 'yellow'),colored('[利用]', 'red'))
    print(colored('7--------------Strace后门', 'yellow'),colored('[利用]', 'red'))
    print(colored('8--------------Rootkit后门', 'yellow'),colored('[检测]', 'blue'))
    print(colored('9--------------不记录命令[history]', 'yellow'), colored('[利用]', 'blue'))
    print(colored('10--------------ssh软链接&crontab', 'yellow'), colored('[利用]', 'red'))
    print(colored('11--------------sshkey密钥&crontab', 'yellow'), colored('[利用]', 'red'))
    print(colored('12--------------php权限维持不死免杀马', 'yellow'), colored('[利用]', 'red'))
    print(colored('13--------------check检查脚本', 'yellow'), colored('[利用]', 'red'))