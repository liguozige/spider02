import re

if __name__ == '__main__':
    #1.替换 sub
    str_one = 'chuanzhi1234'
    str_two = 'a b;fsdfsd,A B'
    pattern = re.compile('\d+')
    result = pattern.sub("",str_one)

    pattern2 = re.compile('(\w+) (\w+)')
    result = pattern2.sub(r'\2 \1',str_two)

    #2.匹配中文 unicode 字符集才能匹配中文
    chinese_str = '小明小红 no'
    chi_pattern = re.compile('[\u4e00-\u9fa5]+')
    result = chi_pattern.findall(chinese_str)

    #3.split分割
    str_thre = 'a,dgdf,,,f;g we fs'
    split_pattern = re.compile('[,; ]+')
    result = split_pattern.split(str_thre)
    
    print(result)
