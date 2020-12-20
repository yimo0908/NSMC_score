# 导入依赖
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
from school_api import SchoolClient

# 获取变量
school_url = os.environ.get('sc_url')        # 教务处外网登陆地址
account = os.environ.get('login_account')    # 教务处登录名
pw = os.environ.get('password')              # 教务处登录密码
mail_user = os.environ.get("mail_account")   # 邮箱账号
mail_pass = os.environ.get("mail_key")       # 邮箱授权码


# 注册一个学校
school = SchoolClient(school_url)
# 实例化一个学生用户
student = school.user_login(account, pw)
# 获取学生信息
info_data = student.get_info()
# 学生信息加格式
sendmsg1 = ("姓名：{real_name}，院系：{faculty}，班级：{class_name}".format(**info_data))
# 获取 2020-2021学年 第一学期 成绩
score_data = student.get_score(score_year='2020-2021', score_term='1')
# dict转str
mystr=str(score_data)
# 定义判断语句
panduan = "{'error': '暂无成绩信息'}"
# 判断
if mystr == panduan:
    sendmsg2 = "别急，成绩还没出"
else:
    # 结构重组
    string = ""
    for i, subject in enumerate(score_data):
        one_subject = "%s学分:%s成绩%s"%(subject["lesson_name"], subject["credit"], subject["score"])
        if subject.get("bkcj") is not None:
            one_subject += "，补考成绩%s"%(subject["bkcj"])
        if subject.get("cxcj") is not None:
            one_subject += "，重修成绩%s"%(subject["cxcj"])
        if i != len(score_data) - 1:
            string += one_subject + ";\n"
        else:
            string += one_subject + ";"
    sendmsg2 = string
# 组合信息
sendmsg = sendmsg1 + "\n" + sendmsg2
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  #设置服务器

sender = mail_user
receivers = [mail_user]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText(sendmsg)
message['From'] = Header("GithubAction", 'utf-8')
message['To'] =  Header("user", 'utf-8')
 
subject = 'Final Exam Score'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
