#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   get_baidu_result.py
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/9 9:54   Jacques Lim    1.0         爬取百度关键词搜索结果
'''

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import random,time

driver_url = r"C:\Users\mayn\AppData\Local\Google\Chrome\Application\chromedriver.exe"
ggzyjy_path = 'C:/Users/mayn/Desktop/ggzyjy.txt'
zfcg_path = 'C:/Users/mayn/Desktop/zfcg.txt'
jsgcjy_path = 'C:/Users/mayn/Desktop/jsgcjy.txt'
jgw_path = 'C:/Users/mayn/Desktop/jgw.txt'
split = '|||||'

def get_links(url):
    '''
    获取一定格式的所有链接
    :param url: 页面url
    :return: 所有链接列表
    '''
    # res = ''
    # try:
    #     res = requests.get(url, timeout=10)
    #     # print(res)
    # except:
    #     print('网页内容获取失败！')
    #     get_links(url)
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(executable_path=driver_url, chrome_options=options)
        browser.set_page_load_timeout(10)
        browser.set_script_timeout(10)
        browser.get(url)
        time.sleep(3)
        try:
            # print("获取的内容是：" + res.text)
            soup = BeautifulSoup(browser.page_source, 'html.parser')
            # print(soup)
            all_containers = soup.find_all(class_='result c-container')
            for one_container in all_containers:
                title = one_container.find('h3').text
                if '百度' in title:
                    continue
                baidu_url = one_container.find(class_='f13').find('a').get('href')
                url = one_container.find(class_='c-showurl').text
                if 'source-icon' in url:
                    url = ''
                with open(jgw_path, 'a+', encoding='utf8')as f:  # 记录各个分类字母分类下各个分页的链接
                    f.write('{}{}{}{}{}\n'.format(title,split,baidu_url,split,url))
                # print(title)
                # print(url)
        except:
            print("获取的HTML内容为空")
    except:
        get_links(url) #出错继续爬同一url

if __name__ == '__main__':
    #爬取百度关键词搜索结果
    url = 'https://www.baidu.com/s?wd=投标监管网&pn={}'
    for i in range(0, 76):
        print('正在爬取第{}页'.format(i))
        get_links(url.format(i*10))
