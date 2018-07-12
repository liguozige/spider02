import json


if __name__ == '__main__':
    json_str = '{"name":"李国丽","age":"18"}'

    #1.将json字符串 转换成python的字典dict list
    json_dict = json.loads(json_str)
    print(json_dict)

    #2.把python字典 list 转成json字符串
    json_dict = {"name":"唐多令","age":19}
    json_str = json.dumps(json_dict)
    print(json_str)

    #3.读取文件json数据，转换成python类型dict  list
    f = open('01data.json','r')
    file = json.load(f)
    print(file)
    #将list dict 写入文件
    f = open('02data.json','w')
    json.dump(json_dict,f)


