#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   url_status.py
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/9 9:54   Jacques Lim    1.0         测试网址是否有效
'''

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import random,time

driver_url = r"C:\Users\mayn\AppData\Local\Google\Chrome\Application\chromedriver.exe"
urls = [
    "http://www.baidu.com/link?url=2pZVyjj30wYCRQ776BItQGAxZtVpjjWPcqlmjasoNZH9uuzuHlMpBv5PQHWsNfhtKj3GaUshjcvhGpOcDCWGYioxJhtcUcUFL53UkTOldo7z6jbb-ST7xeGH7OSPsIZL",
]
split = '|||||'
def get_real_url(url):
    '''
    获取一定格式的所有链接
    :param url: 页面url
    :return: 所有链接列表
    '''
    res = ''
    n = 5
    while(n>0):
        try:
            res = requests.get(url, timeout=10)
            state = (res is not None)
            print('{}{}{}'.format(url,split,state))
            return res
        except:
            print('网页内容获取失败:{}'.format(url))
            n -= 1
            # get_real_url(url)


if __name__ == '__main__':
    #测试网址是否有效
    urls = []
    with open('C:/Users/mayn/Desktop/测试目标爬虫有效链接.txt', 'r', encoding='utf8')as f:
        urls = f.read().split('\n')
    print(urls)
    link = []
    for url in urls:
        get_real_url('http://' + url)
