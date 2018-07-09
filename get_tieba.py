import requests
from randomheaders import randomheaders


class TiebaSpider(object):
    def __init__(self):
        self.tieba_name = input('请输入贴吧名字：')
        self.start_page = int(input('请输入开始页：'))
        self.end_page = int(input('请输入结束页：'))

        self.base_url = "https://tieba.baidu.com/f?"


    #发送请求
    def send_request(self,send_params):
        # headers = {"User-Agent": random.choice(USER_AGENT_LIST)}
        headers = {"User-Agent":randomheaders()}
        print(headers)
        response = requests.get(url=self.base_url,headers = headers,params = send_params)
        data = response.content.decode()
        return data

    #保存数据
    def save_data(self,data,page):
        file_path = 'Tieba_'+str(page)+'页.html'
        print('正在下载第{}页'.format(page))

        with open(file_path,'w')as f:
            f.write(data)

    #调度
    def run(self):
        for page in range(self.start_page,self.end_page+1):


            send_params = {
                'kw':self.tieba_name,
                'pn':(page-1)*50
            }
            #1.发送请求
            data = self.send_request(send_params)
            #2.保存数据
            self.save_data(data,page)


if __name__ == '__main__':
    tool = TiebaSpider()
    tool.run()


