
# encoding:utf-8

import requests
import base64
import os
'''
通用文字识别（高精度版）
'''
# 读取文件
os.chdir('./实验数据集/合同')
catalog = os.listdir()

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
for each in catalog:
# 二进制方式打开图片文件
    f = open(each, 'rb')
    pdf_file = base64.b64encode(f.read())

    params = {"pdf_file":pdf_file}
    access_token = '24.22051f50c4e643b34c98772f80cba6a2.2592000.1659865633.282335-26652690'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        name=each.split('.')[0]
        with open(f'{name}.txt','w') as f:
            f.write(str(response.json()))
        print (response.json())
