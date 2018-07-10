import requests


def renren_profile():

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }

    # 1.代码实现登录
    # 2.找登录url
    # 1.form标签 action = '目标url'
    # 2.如果没有action，抓包 跳转刷新 勾选preserve log
    login_url = 'http://www.renren.com/PLogin.do'

    # 3.拼接登录的参数
    login_data = {
        'email':'18401600683',
        'password':'guo950420'
    }
    # 4.发送登录请求POST
    # session对象 特点是可以自动保存cookie
    session = requests.session()
    session.post(login_url,headers=headers,data=login_data)

    # 5.如果成功  cookie有效
    # 1.目标url 人人好友页面
    profile_url = 'http://www.renren.com/965207546/profile'

    # 发送请求
    data = session.get(profile_url,headers=headers).content.decode()
    # 写入本地
    with open('renren3.html','w') as f:
        f.write(data)


if __name__ == '__main__':
    renren_profile()