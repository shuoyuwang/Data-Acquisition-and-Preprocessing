
# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=V5r4Y6zacG8TYZ5IpuCzS2qO&client_secret=za8LOskDLg0h96o0kQGY3McqCoUb8Uka'
response = requests.get(host)
if response:
    print(response.json())

#24.22051f50c4e643b34c98772f80cba6a2.2592000.1659865633.282335-26652690