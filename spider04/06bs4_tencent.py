from bs4 import BeautifulSoup
from randomheaders import randomheaders
import requests
import json

class TencentSpider(object):
    def __init__(self):
        self.base_url = 'https://hr.tencent.com/position.php'
        self.headers = {"User-Agent":randomheaders()}
        self.data_list = []
        self.page = 0

    #1.发送请求
    def send_request(self,params):
        response = requests.get(self.base_url,headers=self.headers,params=params)
        data = response.content.decode()
        return data


    #2.解析数据  bs4
    """
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=42215&amp;keywords=python&amp;tid=0&amp;lid=2156">OMG097-移动媒体业务运维（北京）</a><span class="hot">&nbsp;</span></td>
        <td>技术类</td>
        <td>3</td>
        <td>北京</td>
        <td>2018-07-13</td>
    </tr>
    """
    def analysis_data(self,data):
        #1.转换成可以解析类型的数据
        html_data = BeautifulSoup(data,'lxml')
        # 2.解析数据 获取所有tr标签的对象 list
        tr_list = html_data.select('.even,.odd')  # 组选择器
        print(tr_list)

        # 3.遍历tr_list中的每一个tr，取出td里面的内容 get_text()
        for tr in tr_list:
            dict_data = {}
            dict_data['work_position'] = tr.select('td a')[0].get_text()
            dict_data['work_class'] = tr.select('td')[1].get_text()
            dict_data['work_count'] = tr.select('td')[2].get_text()
            dict_data['work_place'] = tr.select('td')[3].get_text()
            dict_data['work_time'] = tr.select('td')[4].get_text()
            # 添加到集合list
            self.data_list.append(dict_data)

    #3.保存数据
    def save_data(self):
        json.dump(self.data_list,open('06bs4_tencent.json','w'))
        print('保存成功')

    #4.调度
    def run(self):
        #1.拼接参数
        params = {
            "keywords": "python",
            "lid": "2156",
            "tid": "0",
            "start": "0"
        }
        #2.发送请求
        data = self.send_request(params)
        #3.解析数据
        self.analysis_data(data)

        # 4.保存数据
        self.save_data()

if __name__ == '__main__':
    TencentSpider().run()

