import requests


#反爬 限制频率
class QiushiSpider(object):
    def __init__(self):
        #https://www.qiushibaike.com/8hr/page/3/
        self.base_url = 'https://www.qiushibaike.com/8hr/page/{}'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    #1.組合列表 url
    def get_url_list(self):
        return [self.base_url.format(i) for i in range(1,10)]

    #2.發請求
    def send_request(self,url):
        response = requests.get(url,headers=self.headers)
        data = response.content.decode()
        return data

    #3.解析數據
    def analysis_data(self):
        #1.转换类型


        #2.解析所有的段子
        pass
    #4.保存數據
    def save_data(self,data):
        with open('01qiushi.html','w')as f:
            f.write(data)


    #5.調度
    def run(self):
        # 拼接url
        url_list = self.get_url_list()
        #2.执行循环
        for url in url_list:
            #1.发送请求
            data = self.send_request(url)

            # 2.解析数据

            #3.保存数据
            self.save_data(data)


if __name__ == '__main__':
    QiushiSpider().run()