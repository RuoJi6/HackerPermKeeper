# HackerPermKeeper  
黑客权限保持者<br/><br/>
通过渗透拿到权限之后，为了不让权限丢失，都会进行权限维持，而在进行权限维持的时候，红队需要花费大量的时候，来验证是否合适，因此在这款工具就诞生 HackerPermKeeper[黑客权限保持者] 



| 权限维持模块                 | centos | Ubuntu | 推荐指数 | 备注                                                         |
| :--------------------------- | ------ | ------ | -------- | ------------------------------------------------------------ |
| OpenSSH后门万能密码&记录密码 |   No      | Yes    | ⭐        | 此后门需要很老的内核版本，而且需要很多依赖环境               |
| PAM后门                      | No     | No     | ⭐        | 此后门需要很老的内核版本，而且需要很多依赖环境               |
| SSH软链接                    | Yes    | Yes    | ⭐⭐       | 容易被发现                                                   |
| ssh公私密钥                  | Yes    | Yes    | ⭐⭐⭐⭐⭐    | 发现程度很难，参考了挖矿病毒                                 |
| 后门帐号                     | Yes    | Yes    | ⭐⭐⭐      | 用命令添加账户，不会创建用户home目录[有一个是直接指向root目录] |
| crontab计划任务              | Yes    | Yes    | ⭐⭐⭐⭐     | 难以发现，通过执行计划任务                                   |
| Strace后门                   | Yes    | Yes    | ⭐⭐       | 键盘记录的后门                                               |
| Alias后门                    | Yes    | Yes    | ⭐⭐⭐⭐     | 别名后门，难以发现，但是需要用户去执行命令                   |
| Rootkit后门                  | No     | No     | ⭐⭐⭐      | 难以发现，但是安装复杂，而且指定内核版本                     |

## 🚀 快速使用




# 常见后门介绍
<img width="600" alt="d9f6b995abae8d28bdb35a998a1ec3f" src="https://github.com/ytMuCheng/HackerPermKeeper/assets/79234113/751f0c6c-e995-47ad-b115-eaaa103754d9">



## Stargazers over time [![Stargazers over time](https://starchart.cc/ytMuCheng/HackerPermKeeper.svg)](https://starchart.cc/ytMuCheng/HackerPermKeeper) 




<a href="https://github.com/ytMuCheng">
  <img height=150 align="center" src="https://github-readme-stats.vercel.app/api?username=ytMuCheng"/>
</a>
<a href="https://github.com/ytMuCheng/HackerPermKeeper/">
  <img height=150 align="center" src="https://github-readme-stats.vercel.app/api/top-langs?username=ytMuCheng&layout=compact&langs_count=8&card_width=320" />
</a>
