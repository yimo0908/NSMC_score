# 导入依赖
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
from school_api import SchoolClient

# 获取变量
school_url = os.environ.get('sc_url')
account = os.environ.get('login_account')
pw = os.environ.get('password')
ma = os.environ.get("mail_account")
mp = os.environ.get("mail_key")


# 注册一个学校
school = SchoolClient(school_url)
# 实例化一个学生用户
student = school.user_login(account, pw)
# 获取学生信息
info_data = student.get_info()
print(info_data)
