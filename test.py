import os
import re
import time

import bs4
import requests
from bs4 import BeautifulSoup

# res = requests.get(f'https://github.com/KHwang9883/MobileModels/blob/master/brands/apple.md')

def down():
    url = 'https://github.com/KHwang9883/MobileModels/blob/master/brands/apple.md'
    res = requests.get(url)
    res.raise_for_status()
    # 将页面源码写入本地
    with open('data/result_detailapple.txt', 'wb') as result:
        for line in res.iter_content(200000):
            result.write(line)
    result.close()
    print('保存成功')

# print(soup.select('#readme > article > p:nth-child(5)'))
#通过返回内容取soup
# soup=BeautifulSoup(res.text,'html.parser')
# print(res.text)
#取数据中所有字符串的数据
# for string in soup.stripped_strings:
#     print(repr(string))
# print(name1_detail2)
data=[['A1324','iPhone 3G (国行)'], ['A1303'], ['A1325'], ['A1332'], ['A1332']]
[['默认数据1'],['默认数据2']]

def test():
    soup = bs4.BeautifulSoup(open('data/result_detail.txt', 'r', encoding='utf-8'), 'html.parser')
    # 获取title
    title = soup.select('#readme > article > h1')
    title = ''.join(re.findall(r'</a>(.+?)</h1>', str(title)))
    print(title)
    # name1_1代表如A1324，name1_2代表如iPhone 3G (国行)
    name1 = []
    name2 = []
    for sibling in soup.p.next_siblings:  # 遍历后续节点
        if 'strong' in str(sibling):
            name2.append(str(sibling))
        else:
            name1.append(str(sibling))

    name1 = list(filter(lambda x: x != '\n', name1))
    name1 = list(filter(lambda x: x != '', name1))

    name1_detail1 = []
    # name1_detail2 = []
    # name1中细分name-1，-2
    for i in name1:
        name1_1 = re.findall(r'<p><code>(.+?)</code>', str(i))
        name1_2 = re.findall(r': (.+?)</p>', str(i))
        if name1_1 != '' and name1_2 != '':
            temp = name1_1 + name1_2
            name1_detail1.append(temp)
    print(name1_detail1)

    # print(name1)
    # print(len(name1))
    # print(name2)
    # print(len(name2))

def get360(datas):
    soup = bs4.BeautifulSoup(open('data/result_detail.txt', 'r', encoding='utf-8'), 'html.parser')
    # 获取title
    title = soup.select('#readme > article > h1')
    title = ''.join(re.findall(r'</a>(.+?)</h1>', str(title)))
    print(title)

    # datas = []
    #获取不到值，遍历p标签下的
    # for sibling in soup.p.next_siblings:
    #     # print(sibling)
    #     datas.append(sibling)
    print(len(datas))
    if len(datas) < 1:
        datas.append('append')
        print(datas)
    else:
        print(datas)

    #较笨的写法
    # for i in range(5,55):
    #     print(soup.select(f'#readme > article > p:nth-child({i})'))




#测试数据异常的情况
def test3():
    data = [['A2408', 'iPhone 12 Pro (国行)'], ['A2412', 'iPhone 12 Pro Max (国行)'], [], ['A1219', 'iPad (无线局域网)'], ['A1337', 'iPad (无线局域网 + 3G)']]
    # for i in data:
    #     if i != '':
    #         print(i)
    # out = filter(None,data)
    out = [x for x in data if x]
    print(out)

    testdata = []
    if testdata:
        print('true')
    else:
        print('false')

def test2():
    soup = bs4.BeautifulSoup(open('data/result_detail.txt', 'r', encoding='utf-8'), 'html.parser')
    data1 = soup.select()

def ospath():
    log_path = os.path.dirname(os.path.abspath('.'))
    path2 = os.getcwd()
    t = time.strftime('%Y%m%d_%H%M', time.localtime(time.time()))
    print(log_path)
    print(path2)
    print(t)

datas = [[]]
# down()
# test()
# get360(datas)
# test3()
ospath()