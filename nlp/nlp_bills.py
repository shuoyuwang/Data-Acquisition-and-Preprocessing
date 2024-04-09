

import os
from paddlenlp import Taskflow
from pprint import pprint

schema = ['银行','日期','余额']  # Define the schema for entity extraction

ie = Taskflow('information_extraction', schema=schema)  # 花费时间会安装文件


os.chdir('./实验数据集/银行流水_1')
catalog = os.listdir()
# print(catalog)
# path="./实验数据集/发票/2.txt"

for each in catalog:
    with open(each, "r",encoding='gbk') as f:  # 打开文件
        data = f.read()  # 读取文件
        # print(data)
        pprint(ie(data))
        nlp=ie(data)
        print('------------分割线------------')
    if nlp:
        name = each.split('.')[0]
        with open(f'{name}_nlp.txt', 'w',encoding='gbk') as f:
            f.write(str(nlp))

