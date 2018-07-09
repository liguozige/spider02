import requests
import json

def fanyi_baidu():

    words = input('请输入要翻译的内容：')

    #1.目标url  --移动端 APP
    url = 'http://fanyi.baidu.com/basetrans'
    #注意headers必须是手机的浏览器
    headers = {
        "User-Agent": 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'}
    #2.拼接参数
    data = {
        "query":words,
        "from":"zh",
        "to":"en"
    }
    #3.发送post请求 参数data
    response = requests.post(url,data=data,headers=headers)
    res_data = response.content.decode()
    #4.解析数据 jsonstr--->dict
    dict_data = json.loads(res_data)
    # print(dict_data)
    result = dict_data['trans'][0]['dst']
    # result = dict_data['trans'][0]['result'][0][1]
    print('翻译的结果是：{}'.format(result))

if __name__ == '__main__':
    fanyi_baidu()
