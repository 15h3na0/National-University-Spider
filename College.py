"""
@Author : 15h3na0
@Time : 2020/4/2 16:56
@Blog: https://15h3na0.xyz/
"""
import re
import requests
from openpyxl import workbook


def get_schools():
    url = 'http://www.hao123.com/edu'
    link = []
    tmp = requests.get(url)
    res = re.findall(r'所<a href="(.*?)"', tmp.text)
    for i in res:
        link.append(i)
    return link


def get_urls(url):
    res = []
    for i in url:
        tmp = requests.get(i)
        tmp.encoding = 'gb2312'
        flag = re.findall(r"<p> 　　 <a (href=.*?<\/a>)</p></td>", tmp.text)
        for j in flag:
            res.append(j)
    return res


def to_table(url):
    table = workbook.Workbook()
    data = table.active
    data.append(['学校名称', '官方网站'])
    for i, j in zip(url, range(len(url))):
        if 'baike' in i:
            pass
        else:
            data1 = re.findall(r'href="(.*?)"', i)
            data2 = re.findall(r'>(.*?)<\/a>', i)
            data.append([data2[0], data1[0]])
    table.save('College.xlsx')


if __name__ == '__main__':
    links = get_schools()
    url = get_urls(links)
    to_table(url)
    print('爬取完毕！')