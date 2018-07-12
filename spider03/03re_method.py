import re

if __name__ == '__main__':
    #贪婪模式a-b之间的内容
    str_one = """
        ahhhhhhb
        fsdfsdfsd
        llllllllbB
    """
    #1.创建正则对象
    patter = re.compile('a(.*)b')
    patter = re.compile('a(.*)b',re.DOTALL)  # DOTALL可以匹配换行符
    patter = re.compile('a(.*)b',re.S)  #re.S可以匹配\n
    #忽略大小写 I
    patter = re.compile('a(.*)b',re.S|re.I)
    patter = re.compile('a(.*)b',re.S|re.IGNORECASE)  # I的全拼



    #2.findall
    result = patter.findall(str_one)
    print(result)


    #3.原始字符串
    str_two = r'a\nb'
    str_thre = r'a\bn'
    print(str_thre)
