import requests
from randomheaders import randomheaders
from lxml import etree
import json

class TencentSpider(object):
    def __init__(self):
        #https://hr.tencent.com/position.php?keywords=&tid=0&start=10#a
        self.base_url = 'https://hr.tencent.com/position.php'
        self.headers = {"User-Agent":randomheaders()}
        self.data_list = []
        self.page = 0

    #1.发送请求
    def send_request(self,params):
        response = requests.get(self.base_url,headers=self.headers,params=params)
        data = response.content.decode()
        return data


    #2.解析数据 xpath
    def analysis_data(self,data):
        #1.将字符串转换成element对象,element对象具有xpath的方法，返回的结果是一个列表
        html_data = etree.HTML(data)
        #2.解析数据 获取tr的标签对象 返回的结果是一个list
        tr_list = html_data.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        #3.遍历每一个tr；取出td里面的内容 text()
        """
        <td class="l square"><a target="_blank" href="position_detail.php?id=42394&keywords=python&tid=0&lid=0">25924-运营平台架构师（深圳）</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2018-07-12</td>
        """
        for tr in tr_list:
            data_dict = {}
            data_dict["work_position"] = tr.xpath('//td/a/text()')[0]
            data_dict["work_type"] = tr.xpath('//td[2]/text()')[0]
            data_dict["work_count"] = tr.xpath('//td[3]/text()')[0]
            data_dict["work_place"] = tr.xpath('//td[4]/text()')[0]
            data_dict["work_time"] = tr.xpath('//td[5]/text()')[0]
            #添加到集合list
            self.data_list.append(data_dict)
        #根据下一页标签，判断如果class有值，说明已经是最后一页
        next_class = html_data.xpath('//a[@id="next"]/@class')
        return next_class


    #3.保存数据
    def save_data(self):
        json.dump(self.data_list,open('03tencent4.json','w'))
        print('保存成功')


    #4.调度
    def run(self):
        while True:
            #1.拼参数
            params = {
                "keywords": "python",
                "lid": "2156",
                "tid": "0",
                "start": self.page
            }

            # 2.发送请求
            data = self.send_request(params)
            self.page += 10

            #3.解析数据
            judge_over = self.analysis_data(data)


            #4.如果满足条件class有值，说明已经是最后一页 跳出循环
            if judge_over:
                break

        # 保存数据
        self.save_data()



if __name__ == '__main__':
    TencentSpider().run()