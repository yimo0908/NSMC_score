#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
import requests, base64
from lxml import etree

requests = requests.session()

# 设置变量开始
user_id = input("请输入你的学号：")
user_pwd = input("请输入你的密码：")

url_lan = "http://211.83.41.195/jsxsd/"
url_wan = "https://jiaowu3.nsmc.edu.cn/jsxsd/"

id_base = str(base64.b64encode(user_id.encode('utf-8')))[2:-1]
pwd_base = str(base64.b64encode(user_pwd.encode('utf-8')))[2:-1]
user_encoded = "{}%%%{}".format(id_base, pwd_base)
# 设置变量结束


def login(url):
    # 生成POST数组
    headers = {
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding":
        "gzip, deflate",
        "Accept-Language":
        "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control":
        "max-age=0",
        "Connection":
        "keep-alive",
        "Content-Length":
        "102",
        "Content-Type":
        "application/x-www-form-urlencoded",
        "Host":
        "211.83.41.195",
        "Origin":
        "http://211.83.41.195",
        "Referer":
        "http://211.83.41.195/jsxsd/",
        "Upgrade-Insecure-Requests":
        "1",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"
    }
    data = {
        'userAccount': user_id,
        'userPassword': user_pwd,
        'encoded': user_encoded
    }
    # 执行登陆操作，POST用户信息
    url_login = url + "xk/LoginToXk"
    response = requests.post(url=url_login, headers=headers, data=data)
    # return response.text


def get_score(url):
    """
	获得用户成绩
	按照JSON数组存储
    cjcx_list
	"""
    login(url)
    headers = {
        "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Host":
        "211.83.41.195",
        "Content-Type":
        "application/x-www-form-urlencoded",
        "Origin":
        "http://211.83.41.195",
        "Referer":
        "http://211.83.41.195/jsxsd/kscj/cjcx_query",
        "Upgrade-Insecure-Requests":
        "1",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"
    }
    data = {'kksj': '2020-2021-1', 'kcxz': '', 'kcmc': '', 'xsfs': 'all'}

    # 执行POST信息操作
    url_post = url + "kscj/cjcx_list"
    response = requests.post(url=url_post, headers=headers, data=data)
    response.encoding = 'utf-8'
    score_html = response.text
    score_html = etree.HTML(score_html)

    # 格式化成绩单
    # 偷个懒，想写个while的，但是for省事
    score_dict = {}
    for i in range(2,25):
        score_table = score_html.xpath('//table[@id="dataList"]/tr[{}]/td//text()'.format(i))
    
        if len(score_table) == 0:
            break
        
        score_dict[i-2] = score_table
    print(score_dict)
    # score_dict为所有成绩列表的字典


def output_score(url):
    """
	格式化输出成绩
	调用SMTP发送邮件
	"""
    pass


if __name__ == '__main__':
    while True:
        network = input("输入LAN使用内网，输入WAN使用外网：")
        if network == "WAN" or network == "wan":
            url = url_wan
            break
        elif network == "LAN" or network == "lan":
            url = url_lan
            break
        else:
            pass
    get_score(url)
