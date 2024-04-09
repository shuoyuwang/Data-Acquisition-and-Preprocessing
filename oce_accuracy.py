import windnd
import pyperclip
from tkinter import *

import sys
import json
import base64
import os

from PIL import ImageGrab
from PIL import Image
from io import BytesIO

# 防止https证书校验不正确
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# 保证兼容python2以及python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode
# OCR识别URL
OCR_URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 获取access token
token = "24.22051f50c4e643b34c98772f80cba6a2.2592000.1659865633.282335-26652690"
# 拼接通用文字识别高精度url
image_url = OCR_URL + "?access_token=" + token


# 读取文件
def read_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        return f.read()
    except:
        print('read image file fail')
        return None
    finally:
        if f:
            f.close()


# 调用远程服务
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        if (IS_PY3):
            result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)


def copy():
    contents = text.get(1.0, END)
    pyperclip.copy(contents)


def clip_img():
    pic = ImageGrab.grabclipboard()
    # pic.show()
    output_buffer = BytesIO()
    pic.save(output_buffer, "png")
    byte_data = output_buffer.getvalue()
    base64_img = base64.b64encode(byte_data).decode('utf-8')
    print(base64_img)
    content_text = ""
    # 调用文字识别服务
    result = request(image_url, urlencode({'image': base64_img}))
    # 解析返回结果
    result_json = json.loads(result)
    print(result_json)
    for words_result in result_json["words_result"]:
        content_text += words_result["words"] + "\n"
    # 打印文字
    text.insert(INSERT, content_text)
    print(content_text)


# 清空文本框的所有内容
def empty():
    text.delete(1.0, END)


# 拖拽识别
def dragged_files(files):
    msg = '\n'.join((item.decode('gbk') for item in files))
    msg = msg.replace("\\", "/")
    content_text = ""
    # 读取测试图片
    file_content = read_file(msg)
    # 每次获取一行
    content_text = ""
    # 调用文字识别服务
    result = request(image_url, urlencode({'image': base64.b64encode(file_content)}))
    # 解析返回结果
    result_json = json.loads(result)
    for words_result in result_json["words_result"]:
        content_text += words_result["words"] + "\n"
    # 打印文字
    text.insert(INSERT, content_text)
    print(content_text)


# 界面
from tkinter import *

root = Tk()  # 创建根窗口
root.title('准确识别ocr')
f1 = Frame(root)
f1.pack()
f2 = Frame(root)
f2.pack()

lb1 = Label(f1, text="识别结果:", anchor=W, justify=LEFT)
lb1.pack(fill=X, padx=10, pady=5)
sb1 = Scrollbar(f1)
sb1.pack(side=RIGHT, fill=Y)
text = Text(f1, width=70, height=20, bg="#CAE1FF", relief="solid", font=14, yscrollcommand=sb1.set)  # 创建多行文本框
text.pack(padx=10, pady=5)  # 包装文本框，没有此步骤，文本框无法显示在窗口中
sb1.config(command=text.yview)
# 插入组件
bt1 = Button(f2, text='清空', command=empty)  # 创建按钮
bt1.pack(side=LEFT, padx=50, pady=10)
bt2 = Button(f2, text='粘贴', command=clip_img)  # 创建按钮
bt2.pack(side=LEFT, padx=50, pady=10)
bt3 = Button(f2, text='复制', command=copy)  # 创建按钮
bt3.pack(side=LEFT, padx=50, pady=10)
windnd.hook_dropfiles(root, func=dragged_files)
root.mainloop()
