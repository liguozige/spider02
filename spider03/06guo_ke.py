import requests
import re

class GuokeSpider(object):
    def __init__(self):
        self.url = 'https://www.guokr.com/ask/hottest/?page=2'
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36"}

        #正则：保持原始字符串 符号
        #<h2><a target="_blank" href=(.*)>(.*)</a></h2>
        self.pattern = re.compile('<h2><a target="_blank" href=(.*)>(.*)</a></h2>')


    #1.发请求
    def send_request(self):
        data = requests.get(self.url,headers=self.headers).content.decode()
        return data

    # 2.解析数据
    def analysis_data(self,data):
        result_list = self.pattern.findall(data)
        return result_list

    #3.保存文件
    def write_file(self,data):
        with open('06guo.html','w')as f:
            f.write(data)
            print('写入成功')
    #4.run
    def run(self):
        data = self.send_request()
        result_list = self.analysis_data(data)
        print(result_list)
        self.write_file(data)


if __name__ == '__main__':
    GuokeSpider().run()