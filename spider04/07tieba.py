import requests
from lxml import etree
from randomheaders import randomheaders


#图片查找的过程： 1.贴吧列表首页——>2.每个帖子的详情页——>3.目标图片请求
class TiebaSpider(object):
    def __init__(self):
        self.tieba_name = '美食'
        self.base_url = 'http://tieba.baidu.com/f?kw=美食吧&pn=0'
        # self.base_url = 'http://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F&ie=utf-8&pn=50'
        # self.headers = {"User-Agent":randomheaders()}
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 1.第一层解析 详情页的xpath 返回的是list
        self.first_xpath = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        # 2.第二层解析 图片xpath
        self.second_xpath = '//img[@class="BDE_Image"]/@src'

    # 1.发送请求
    def send_request(self,url):
        response = requests.get(url,headers=self.headers)
        data = response.content
        return data

    def analysis_data(self,first_data,xpath_str):
        # 1.转换类型
        html_data = etree.HTML(first_data)
        # 2.解析数据
        result_list = html_data.xpath(xpath_str)
        return result_list


    # 2.保存本地文件
    def save_data(self,image_name,data):
        file_name = 'images/'+image_name
        print(file_name)
        with open(file_name,'wb')as f:
            f.write(data)

    def run(self):
        #1.发送请求
        first_data = self.send_request(self.base_url)
        with open('tieba.html','wb')as f:
            f.write(first_data)
        # print(first_data)
        # 2.发送详情页的请求
        # 2.1详情页的url
        details_url_list = self.analysis_data(first_data,self.first_xpath)
        print(details_url_list)
        # 2.2发送请求
        for link in details_url_list:
            url = 'http://tieba.baidu.com'+link
            # 发送请求
            details_data = self.send_request(url)
            print(details_data)
            # 3.请求图片
            img_url_list = self.analysis_data(details_data,self.second_xpath)
            print(img_url_list)
            for img_url in img_url_list:
                image_data = self.send_request(img_url)
                # 保存图片
                image_name = img_url[-11:]
                self.save_data(image_name,image_data)

            print('保存成功')

        print('保存完毕')


if __name__ == '__main__':
    TiebaSpider().run()