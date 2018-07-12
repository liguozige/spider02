import re

if __name__ == '__main__':
    str_one = '123abc'
    str_two = '456'
    pattern = re.compile('^\d+$')

    #1.match 从头开始，匹配一次
    result = pattern.match(str_two)
    print(result.group())
    #2.search 从任意位置
    result = pattern.search(str_two)
    print(result.group())

    #3.findall 返回list
    str_two = 'asffewfsafdsaewf'
    pattern = re.compile('s')
    result = pattern.findall(str_two)
    print(result)


    #4.finditer  --iter
    result = pattern.finditer(str_two)
    for res in result:

        print(res.group())
    print(result)
