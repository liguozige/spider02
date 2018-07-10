import requests


def renren_profile():
    #1.目标url 人人好友页面
    profile_url = 'http://www.renren.com/965207546/profile'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }
    #发送请求
    data = requests.get(profile_url,headers=headers).content.decode()
    #写入本地
    with open('renren.html','w')as f:
        f.write(data)


if __name__ == '__main__':
    renren_profile()