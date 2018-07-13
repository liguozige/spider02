from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    html_data = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <p class="story">...</p>
    """

    #1.转换类型
    soup = BeautifulSoup(html_data,'lxml')

    #2.解析标签数据 find  find_all  select

    #3.find  符合条件的第一个标签
    result = soup.find(name='p')
    result = soup.find(attrs={'id':'link2'})
    result = soup.find(text='...')
    pattern = re.compile('^a')
    result = soup.find(pattern)

    #4.find_all 返回列表
    result = soup.find_all('a')


    #5.select css选择器；返回列表list
    #标签 类 ID 层级后代  组选择器  属性选择器
    result = soup.select('title')  # 标签选择器
    result = soup.select('.title')  # 类选择器
    result = soup.select('#link1')  # ID选择器
    result = soup.select('p a')  # 层级后代选择器 p标签下的a标签
    result = soup.select('head,title')  # 组选择器
    result = soup.select('a[id="link2"]')  # 属性选择器
    #6.找标签包裹的内容 get_text()
    result = soup.select('a[id="link2"]')[0].get_text()

    #7.属性 get('属性名称')
    result = soup.select('a[id="link2"]')[0].get('href')

    print(result)