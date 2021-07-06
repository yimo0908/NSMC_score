import requests
from bs4 import BeautifulSoup
import base64

requests = requests.session()


def login(user, passwd):
    us = str(base64.b64encode(user.encode('utf-8'))).strip('b').replace("'", '')
    ps = str(base64.b64encode(passwd.encode('utf-8'))).strip('b').replace("'", '')
    url = 'http://211.83.41.195/jsxsd/xk/LoginToXk'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Length": "102",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "211.83.41.195",
        "Origin": "http://211.83.41.195",
        "Referer": "http://211.83.41.195/jsxsd/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"}

    data = {'userAccount': user,
            'userPassword': passwd,
            'encoded': f"{us}%%%{ps}"}

    response = requests.post(url=url, headers=headers, data=data)

    response.encoding = 'utf-8'
    html = response.text
    return html


def get_grade(user, passwd):
    login(user, passwd)
    url = 'http://211.83.41.195/jsxsd/kscj/cjcx_list'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Host": "211.83.41.195",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://211.83.41.195",
        "Referer": "http://211.83.41.195/jsxsd/kscj/cjcx_query",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"}
    data = {'kksj': '2020-2021-1',
            'kcxz': '',
            'kcmc': '',
            'xsfs': 'all'}
    response = requests.post(url=url, headers=headers, data=data)
    response.encoding = 'utf-8'
    # soup = BeautifulSoup(response.text, 'html.parser')
    # kenames = soup.find_all("td", align="left")
    # names = []
    # grades = []
    # for num in range(1, kenames.__len__(), 2):
    #     kename = kenames[num].text
    #     names.append(kename)
    # for num in range(0, grades_text.__len__()):
    #     grade = grades_text[num].text.strip()
    #     grades.append(float(grade))
    #
    # txt = dict(zip(names, grades))
    # grades.sort(reverse=True)
    # data = ''
    # for key, value in txt.items():
    #     data += ('{}  {}分\n'.format(key, value))
    #
    # data = f'你的成绩查询结果如下:\n{data}'

    requests.close()
    return data


if __name__ == '__main__':
    us = ''  # 学号
    ps = ''  # 密码
    print(get_grade(us, ps))
