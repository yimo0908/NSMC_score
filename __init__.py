#! /usr/bin/python
# -*- coding: utf-8 -*-
#
import requests, base64


# 设置变量开始
user_id = input("请输入你的学号：")
user_pwd = input("请输入你的密码：")

url_lan = "http://211.83.41.195/jsxsd/xk/LoginToXk"
url_wan = "https://jiaowu3.nsmc.edu.cn/jsxsd/xk/LoginToXk"

id_base = str(base64.b64encode(user_id.encode('utf-8')))[2:-1]
pwd_base = str(base64.b64encode(user_pwd.encode('utf-8')))[2:-1]
user_encoded = "{}%%%{}".format(id_base, pwd_base)
# 设置变量结束

# 生成POST数组
headers = {
			}

data = {'userAccount': user_id,
        'userPassword': user_pwd,
        'encoded': user_encoded}

def login_def():
	"""
	用户登陆函数
	生成
	POST http302
	无响应
	"""
	pass


def get_score():
	"""
	获得用户成绩
	按照JSON数组存储
	"""
	pass


def output_score():
	"""
	格式化输出成绩
	调用SMTP发送邮件
	"""
	pass



if __name__ == '__main__':
	print(data)
