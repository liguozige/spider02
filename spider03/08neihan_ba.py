import requests
import re
from randomheaders import randomheaders

class NeihanBaSpider(object):
    def __init__(self):
        self.base_url = 'https://www.neihan8.com/article/index_'
        self.headers = {"User-Agent": randomheaders()}
        self.first_pattern = re.compile('<div class="desc">(.*?)</div>')
        self.second_pattern = re.compile('<(.*)|\s|&(.*?);>')
    # 1.发请求
    def send_request(self,url):
        response = requests.get(url,headers=self.headers)
        data = response.content.decode()
        return data

    #2.解析
    def analysis_data(self,data):
        result_list = self.first_pattern.findall(data)
        return result_list

    #3.保存文件
    def save_file(self,data_list,page):
        page = '-------------------------------第' + str(page) + '页' + '--------------------------------------------\n\n'
        print(page)

        with open('08neihanba.html','a') as f:
            f.write(page)
            for content in data_list:
                new_cotent = self.second_pattern.sub('',content) + '\n'
                f.write(new_cotent)
        print('写入成功')

    def get_url_list(self):
        url_list = []
        for page in range(1,5):
            url = self.base_url + str(page) + '.html'
            url_list.append(url)
        return url_list



    #4.run
    def run(self):
        #拼接url

        url_list = self.get_url_list()
        for url in url_list:
            #1.发送请求
            data = self.send_request(url)
            #2.解析数据
            data_list = self.analysis_data(data)
            #2.保存
            page = url_list.index(url)+1
            self.save_file(data_list,page)



if __name__ == '__main__':
    NeihanBaSpider().run()
