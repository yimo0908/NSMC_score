# 导入依赖
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header

# 获取变量
account = os.environ.get('login_account')    # 教务处登录名
pw = os.environ.get('password')              # 教务处登录密码
mail_user = os.environ.get("mail_account")   # 邮箱账号
mail_pass = os.environ.get("mail_key")       # 邮箱授权码
term = os.environ.get('score_term')          # 要查询的学期

sendmsg = ""
# 第三方 SMTP 服务
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
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
