from bs4 import BeautifulSoup


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

    #1.转换类型   指定解析类型是lxml 如果不指定，默认也是lxml只不过是有警告
    soup = BeautifulSoup(html_data,'lxml')

    #2.格式化  该缩进的缩进，该嵌套的嵌套，该补齐的补齐
    print(soup.prettify())
