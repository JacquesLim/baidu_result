#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   get_real_url.py
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/9 9:54   Jacques Lim    1.0         None
'''

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import random,time

driver_url = r"C:\Users\mayn\AppData\Local\Google\Chrome\Application\chromedriver.exe"
urls = [
   #此处填入百度提供的结果链接

]
split = '|||||'
def get_real_url(url):
    '''
    获取一定格式的所有链接
    :param url: 页面url
    :return: 所有链接列表
    '''
    res = ''
    try:
        res = requests.get(url, timeout=10).url
        print('{}{}{}'.format(url,split,res))
        return res
    except:
        print('网页内容获取失败:{}'.format(url))
        # get_real_url(url)


if __name__ == '__main__':
    #输出真实地址
    link = []
    for url in urls:
        link.append(get_real_url(url))
    print(link)
