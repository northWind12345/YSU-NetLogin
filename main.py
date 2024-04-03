import requests
from urllib.parse import quote
import time
import smtplib
from email.mime.text import MIMEText


def smtp(to_addr,from_addr,from_password):
    msg = MIMEText('start!','plain','utf-8')
    msg['From'] = from_addr
    msg['to'] = to_addr
    msg['Subject'] = "Start!"

    if 'qq' in from_addr:
        smtpObj = smtplib.SMTP_SSL('smtp.qq.com',465)
    elif '163' in from_addr:
        smtpObj = smtplib.SMTP_SSL('smtp.163.com', 465)
    else:
        print('请正确输入用于发送邮件的QQ或163邮箱！')
        input()
        exit(0)

    smtpObj.login(from_addr,from_password)
    smtpObj.sendmail(from_addr,to_addr,msg.as_string())
    smtpObj.quit()

with open('info.txt','r',encoding="utf-8") as f:
    data = f.read().splitlines()
while '' in data:
    data.remove('')
if len(data) == 4:
    userId,password,service,cookies_url = data
    is_seed = False
elif len(data) == 7:
    userId, password, service, cookies_url, f_addr, f_password, t_addr = data
    is_seed =True
else:
    print('请正确设置info.txt文件')
    input()
    exit(0)

queryString =cookies_url.split('?')[1]
queryString = quote(queryString)
service = quote(service)
login_url = 'https://auth.ysu.edu.cn:8443/eportal/InterFace.do?method=login'
User_Agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
login_data = {'userId':userId, 'password':password, 'service':service, 'queryString':queryString, 'operatorPwd':'','operatorUserId':'','validcode':'', 'passwordEncrypt':'false'}
login_response = requests.post(login_url,data=login_data,headers={'User-Agent':User_Agent})

time.sleep(10)
code = requests.get('https://www.baidu.com').status_code
if code == 200:
    print('连接成功！')
else:
    print('没有连接成功，请详细检查！')
if is_seed:
    smtp(t_addr,f_addr,f_password)
    print('邮件已发送！')
print('5秒后自动关闭窗口！')
time.sleep(5)


