import requests

def fanyi_baidu():

    #1.目标url  --移动端 APP
    url = 'http://fanyi.baidu.com/basetrans'
    #注意headers必须是手机的浏览器
    headers = {
        "User-Agent": 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'}
    #2.拼接参数
    data = {
        "query":"葡萄",
        "from":"zh",
        "to":"en",
    }
    #3.发送post请求 参数data
    response = requests.post(url,data=data,headers=headers)
    res_data = response.content.decode()
    #4.验证
    print(res_data)

if __name__ == '__main__':
    fanyi_baidu()
