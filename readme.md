<font face="逐浪立楷" color=blue size=10>YSU-NetLogin</font>

# 此脚本目的是为了方便使用校园网的情况下，进行远程办公

此项目中main.py为源码，main.exe为封装后的可执行程序，完成下面的配置后main.exe可以直接使用，确保info.txt和main.py、main.exe在同一路径下。将main.exe的快捷方式放到Windows系统的开始菜单，实现开机自动联网。通过计划任务实现定时连接网络，或定时开机。也可在BIOS中设置上电开机。之后配合远程班办公软件使用。

## 1.基本使用方法

脚本有两种使用方法，一种直接连接校园网账号，另一种连接校园网后进行邮箱提醒

### 1.1 直接连接校园网

![校园网界面](https://raw.githubusercontent.com/northWind-666/YSU-NetLogin/master/img/%E6%A0%A1%E5%9B%AD%E7%BD%91%E7%95%8C%E9%9D%A2.png)

在info.txt中输入

1. 第一行输入用户名

2. 第二行输入密码

3. 第三行输入 中国联通/中国移动/中国电信/校园网 ![运营商](https://github.com/northWind-666/YSU-NetLogin/raw/master/img/运营商.png)

4.  第四行输入网页连接，每台电脑连接不同

最终的info.txt配置如

![info.txt配置](https://github.com/northWind-666/YSU-NetLogin/raw/master/img/直接连接.png)

### 1.2 发送邮件

发送邮件要比直接连接多三行配置

5. 输入用于发送邮件的邮箱

6. 输入发送邮箱的SMTP密码（**此密码非邮箱登录密码，具体密码设置请看[2.邮箱的SMTP登录](#2.邮箱的SMTP登录)，支持QQ和163邮箱**）
7. 输入用于接收邮件的邮箱

最终的info.txt配置如

![info.txt配置](https://github.com/northWind-666/YSU-NetLogin/raw/master/img/发送邮件.png)

## 2.邮箱的SMTP登录

### 2.1 QQ邮箱SMTP登录

可以参考教程[帮助系统 (qq.com)](https://service.mail.qq.com/detail/128/53?expand=14)

### 2.2 163邮箱SMTP登录

和QQ邮箱设置差不多[帮助中心_常见问题 (163.com)](https://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac25ef2e192b234ae4d)



