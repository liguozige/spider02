import requests


def ssl_verify_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }

    # 12306证书 不是第三方认证，浏览器会警告拦截
    url = 'https://www.12306.cn/mormhweb/'

    #告诉系统