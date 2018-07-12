from lxml import etree

if __name__ == '__main__':
    html_str = '''
    <div>
    <p class='one' id='first'></p>
    <ul>
    <li class="item-1"><a href="link1.html">first item</a></li>
    <li class="item-1"><a href="link2.html">second item</a></li>
    <li class="item-inactive"><a href="link3.html">third item</a></li>
    <li class="item-1"><a href="link4.html">fourth item</a></li>
    <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
    </ul> </div>

    '''


    #1.转换成可解析的类型
    html_data = etree.HTML(html_str)

    #2.解析数据 xpath('//a')   返回的是列表list
    result = html_data.xpath('//li')

    result = html_data.xpath('//a')
    #取出标签包裹的内容 text()
    result = html_data.xpath('//li[@class="item-inactive"]/a/text()')
    # result = html_data.xpath('//a[@href="link3.html"]/text()')[0]

    #取标签的属性 @属性名
    result = html_data.xpath('//p/@id')
    result = html_data.xpath('//li[1]')

    print(result)

    #3.格式化 补全
    all_data = etree.tostring(html_data)  # byte类型

    # print(all_data.decode())