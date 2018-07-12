import requests
import re
from randomheaders import randomheaders
import json


def load_data_36_kr():
    #1.url
    url = 'http://36kr.com/'
    #2.headers
    headers = {"User-Agent":randomheaders()}
    #3.发送请求
    data = requests.get(url,headers=headers).content.decode()
    #4.解析数据 <script>var props={},locationnal={}</script>
    pattern = re.compile('<script>var props=(.*),locationnal=')
    result = pattern.findall(data)
    #5.保存文件
    with open('07kr.json','w')as f:
        f.write(result[0])
    print(result[0])
    json.loads(result[0])


if __name__ == '__main__':
    load_data_36_kr()
