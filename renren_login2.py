import requests


def renren_profile():
    #1.目标url 人人好友页面
    profile_url = 'http://www.renren.com/965207546/profile'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }
    #2.通过cookies参数传递字典
    cook_str = "anonymid=jje899ltdfuzza; depovince=BJ; _r01_=1; JSESSIONID=abcVLNAhWrF7j6jDy9_rw; ick_login=301da3e6-20c0-4fc8-8b24-7a4fb986b52d; wp_fold=0; _ga=GA1.2.1810012430.1531142942; _gid=GA1.2.1557756918.1531142942; XNESSESSIONID=5ba39796910f; wp=0; BDTUJIAID=dc2fd8252ba86b460ca7458694c3db63; ick=f75deb22-b22f-4bb5-b577-2a830a1ef8bc; jebecookies=60cd18a8-e900-4225-a910-fe07b5c04bb2|||||; _de=5E62B926E485207B2C5171BA5F2BB7A4; p=e9247d3566e20a85727688e6a24734d28; first_login_flag=1; ln_uact=18401600683; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=283889727ca67cd9e8d45bfddecccdcf8; societyguester=283889727ca67cd9e8d45bfddecccdcf8; id=966864628; xnsid=7e1ddded; ver=7.0; loginfrom=null; jebe_key=add74965-3a1c-4825-a6a3-30a637020d67%7Cd27e91ff3d42d005a0bc6f857acfa94a%7C1531187438969%7C1%7C1531187441099; l4pager=0; WebOnLineNotice_966864628=1"
    #3.将cookie字符串转成字典
    cook_dict = {
        "jebecookies":"60cd18a8-e900-4225-a910-fe07b5c04bb2|||||",
        "_de":"5E62B926E485207B2C5171BA5F2BB7A4",
        "p":"e9247d3566e20a85727688e6a24734d28",
        "first_login_flag":"1",
        "ln_uact":"18401600683",
        "ln_hurl":"http://head.xiaonei.com/photos/0/0/men_main.gif",
        "t":"283889727ca67cd9e8d45bfddecccdcf8",
        "societyguester":"283889727ca67cd9e8d45bfddecccdcf8",
        "id":"966864628",
        "xnsid":"7e1ddded",
        "ver":"7.0",
        "loginfrom":"null",
        "jebe_key":"add74965-3a1c-4825-a6a3-30a637020d67%7Cd27e91ff3d42d005a0bc6f857acfa94a%7C1531187438969%7C1%7C1531187441099",
        "l4pager":"0",
        "WebOnLineNotice_966864628":"1"
    }


    #发送请求
    data = requests.get(profile_url,headers=headers,cookies=cook_dict).content.decode()

    #写入本地
    with open('renren2.html','w')as f:
        f.write(data)


if __name__ == '__main__':
    renren_profile()