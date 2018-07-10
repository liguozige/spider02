import requests


def renren_profile():
    #1.目标url 人人好友页面
    profile_url = 'http://www.renren.com/965207546/profile'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        'Cookie': 'anonymid=jje899ltdfuzza; depovince=BJ; _r01_=1; JSESSIONID=abcVLNAhWrF7j6jDy9_rw; ick_login=301da3e6-20c0-4fc8-8b24-7a4fb986b52d; loginfrom=null; wp_fold=0; _ga=GA1.2.1810012430.1531142942; _gid=GA1.2.1557756918.1531142942; XNESSESSIONID=5ba39796910f; wp=0; BDTUJIAID=dc2fd8252ba86b460ca7458694c3db63; ick=f75deb22-b22f-4bb5-b577-2a830a1ef8bc; t=47d294c59e646aefd79956a43e1a75f44; societyguester=47d294c59e646aefd79956a43e1a75f44; id=966859454; xnsid=7e2b443c; jebecookies=1ec96b0c-89d5-40ba-baec-9cdfc953cebe|||||; ver=7.0; jebe_key=add74965-3a1c-4825-a6a3-30a637020d67%7Cd5b5148dfcca63e2cc3679033a7953e0%7C1531186560906%7C1%7C1531186562986'
    }
    #发送请求
    data = requests.get(profile_url,headers=headers).content.decode()
    #写入本地
    with open('renren.html','w')as f:
        f.write(data)


if __name__ == '__main__':
    renren_profile()