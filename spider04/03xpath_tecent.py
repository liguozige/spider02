import requests
from randomheaders import randomheaders

class TencentSpider(object):
    def __init__(self):
        #https://hr.tencent.com/position.php?keywords=&tid=0&start=10#a
        self.base_url = 'https://hr.tencent.com/position.php'
        self.headers = {"User-Agent":randomheaders()}

    #1.发送请求
    def send_request(self,params):
        response = requests.get(self.base_url,headers=self.headers,params=params)
        data = response.content.decode()
        return data


    #2.解析数据 xpath


    #3.保存数据
    def save_data(self,data):
        with open('03tencent.html','w') as f:
            f.write(data)



    #4.调度
    def run(self):
        #1.发送请求

        params = {
            "keywords": "python",
            "lid": "0",
            "tid": "0",
        }

        data = self.send_request(params)

        #2.解析数据


        #3.保存数据
        self.save_data(data)



if __name__ == '__main__':
    TencentSpider().run()