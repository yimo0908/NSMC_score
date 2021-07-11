import base64
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText

import requests
from lxml import etree

requests = requests.session()

# 设置变量开始
user_id = os.environ.get('login_account')   # 教务系统登录账号
user_pwd = os.environ.get('password')   # 教务系统登录密码
term = os.environ.get('score_term')    # 查分学期
mail_user = os.environ.get("mail_account")  # 邮箱账号
mail_pass = os.environ.get("mail_key")  # 邮箱授权码
url_wan = "https://jiaowu3.nsmc.edu.cn/jsxsd/"

id_base = str(base64.b64encode(user_id.encode('utf-8')))[2:-1]
pwd_base = str(base64.b64encode(user_pwd.encode('utf-8')))[2:-1]
user_encoded = "{}%%%{}".format(id_base, pwd_base)


# 设置变量结束


def login(url):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "max-age=0",
        "content-length": "124",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://jiaowu3.nsmc.edu.cn",
        "referer": "https://jiaowu3.nsmc.edu.cn/jsxsd/",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67"
    }
    data = {
        'userAccount': user_id,
        'userPassword': user_pwd,
        'encoded': user_encoded
    }
    url_login = url + "xk/LoginToXk"
    _res = requests.post(url=url_login, headers=headers, data=data)


def get_score(url):
    # 获得用户成绩
    login(url)
    headers = {
        "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Content-Type":
            "application/x-www-form-urlencoded",
        "Origin":
            "https://jiaowu3.nsmc.edu.cn",
        "Referer":
            "https://jiaowu3.nsmc.edu.cn/jsxsd/kscj/cjcx_query",
        "Upgrade-Insecure-Requests":
            "1",
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"
    }
    data = {'kksj': {term}, 'kcxz': '', 'kcmc': '', 'xsfs': 'all'}
    url_post = url + "kscj/cjcx_list"
    response = requests.post(url=url_post, headers=headers, data=data)
    response.encoding = 'utf-8'
    score_html = response.text
    score_html = etree.HTML(score_html)

    # 格式化成绩单
    score_dict = {}
    for i in range(2, 25):
        score_table = score_html.xpath('//table[@id="dataList"]/tr[{}]/td//text()'.format(i))
        if len(score_table) == 0:
            break
        score_table[4] = score_table[4].replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '')
        score_dict[i - 2] = score_table
    a = ""
    li_1 = [elem[3] for elem in score_dict.values()]
    li_2 = [elem[11] for elem in score_dict.values()]
    li_3 = [elem[4] for elem in score_dict.values()]
    for i in range(len(li_1)):
        a += ("%s  %s  %s" % (li_1[i], li_2[i], li_3[i])) + "\n"
    return a


def mail(url):
    # 发送邮件
    sendmsg = get_score(url)
    mail_host = "smtp.qq.com"  # 设置服务器
    sender = mail_user
    receivers = [mail_user]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText(sendmsg)
    message['From'] = Header("GithubAction", 'utf-8')
    message['To'] = Header("user", 'utf-8')
    subject = 'Final Exam Score'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    print(mail(url_wan))
