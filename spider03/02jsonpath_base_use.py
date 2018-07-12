import requests
import jsonpath
import json


def jsonpath_use():
    #1.url
    url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }
    #2.发送请求
    response = requests.get(url,headers=headers)
    data = response.content.decode()

    #如果有url 尾缀是.json 使用.json() --返回来的结果就是dict
    json_data = response.json()
    #3.解析数据 jsonpath传参传入的是dict或者list
    #3.1 转成dict
    dict_data = json.loads(data)
    #3.2 jsonpath解析 返回的是list
    result = jsonpath.jsonpath(json_data,'$..name')

    print(result)


if __name__ == '__main__':
    jsonpath_use()
