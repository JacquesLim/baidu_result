#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   get_jianyu.result.py    
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/7/1 13:32   Jacques Lim    1.0         None
'''

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import random,time,re
from fake_useragent import UserAgent
from lxml import html
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver_url = r"C:\Users\mayn\AppData\Local\Google\Chrome\Application\chromedriver.exe"


def get_proxy():
    proxy = requests.get("http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=1&time=1&pro=&city=&port=1&format=txt&ss=1&css=&dt=1&specialTxt=3&specialJson=").text
    return proxy

def get_zbqy_gg_result(url, keyword):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless') #不弹出浏览器
    ua = UserAgent()
    useragent = ua.chrome
    options.add_argument('--user-agent={}'.format(useragent))
    proxy = get_proxy()
    # print(proxy)
    # print(useragent)
    if ':' not in proxy:
        time.sleep(60)
        return None
    options.add_argument('--proxy-server=http://{}'.format(proxy))
    options.add_argument(r'--user-data-dir=C:\Users\mayn\AppData\Local\Google\Chrome\User Data')
    # options.add_cookie(session.sessions)
    prefs = {
        'profile.default_content_setting_values': {'images': 2, }
    }
    options.add_experimental_option("prefs", prefs)
    browser = webdriver.Chrome(driver_url, 0, options)
    browser.set_page_load_timeout(20)
    browser.set_script_timeout(20)
    count = 1
    # time.sleep(random.randint(3, 6))
    try:
        browser.get(url)
        time.sleep(random.randint(2, 4))
    except:
        browser.quit()
        return None
    # time.sleep(random.randint(3, 6))
    try:
        browser.find_element_by_xpath('//*[@id="searchinput"]').send_keys(keyword)
        time.sleep(random.randint(2, 3))
    except:
        browser.quit()
        return None

    ActionChains(browser).move_by_offset(random.randint(100, 200), random.randint(100, 200)).click().perform()  # 鼠标左键点击， 200为x坐标， 100为y坐标
    time.sleep(random.randint(2, 3))

    # try:
    #     browser.find_element_by_xpath('//*[@id="searchinput"]').send_keys(Keys.ENTER)
    # except:
    #     browser.quit()
    #     return None
    # try:
    #     browser.find_element_by_xpath('//*[@id="zbSeatchT"]/input[2]').click()
    # except:
    #     browser.find_element_by_xpath('//*[@id="zbSeatchT"]/input[2]').click()
    # time.sleep(random.randint(3,6))
    # browser.find_element_by_xpath('//*[@id="zbSeatchT"]/input[2]').click()
    time.sleep(random.randint(2,4))
    table_html = browser.find_element_by_xpath('// *[ @ id = "formTable"]').text
    # print(table_html)
    com = re.compile(r'(\d+) ')  # 匹配“id”
    try:
        max_id = int(com.findall(table_html)[-2])
    except:
        browser.quit()
        return -1
    print(max_id)

    first_handle = browser.current_window_handle
    url_list = []
    if max_id == 1:
        xp = '//*[@id="formTable"]/tr/td[3]'
        browser.find_element_by_xpath(xp).click()
        # print(html)
        time.sleep(random.randint(3,5))
        handles = browser.window_handles
        browser.switch_to.window(handles[-1])  # 切换到最新窗口的句柄
        try:
            new_html = browser.page_source
        except:
            print('出错企业：{}'.format(keyword))
            browser.quit()
            return None
        soup = BeautifulSoup(new_html, 'html.parser')
        new_url = soup.find(class_='original-text').find('a').get('href')
        url_list.append(new_url)
    else:
        for i in range(1, max_id+1):
            if i%10 == random.randint(7,12): #页数太多,缓一下
                time.sleep(20)
            xp = '//*[@id="formTable"]/tr[{}]/td[3]'.format(i)
            browser.find_element_by_xpath(xp).click()
            # print(html)
            time.sleep(random.randint(1,3))
            handles = browser.window_handles
            browser.switch_to.window(handles[-1])  # 切换到最新窗口的句柄
            # soup = BeautifulSoup(browser.page_source, 'html.parser')
            # print(new_html)
            try:
                new_html = browser.page_source
                soup = BeautifulSoup(new_html, 'html.parser')
                new_url = soup.find(class_='original-text').find('a').get('href')
                url_list.append(new_url)
                browser.close()
                browser.switch_to.window(first_handle)  # 切换到第一个窗口的句柄
            except:
                browser.close()
                browser.switch_to.window(first_handle)  # 切换到第一个窗口的句柄
                continue

            # print(new_url)
    browser.quit()
    return url_list
    # except:
    #     # delete_proxy(proxy)
    #     # return get_zbqy_gg_result(url, keyword)
    #     browser.quit()
    #     return None

if __name__ == '__main__':

    path = r'C:\Users\mayn\Desktop\公司\产品工作\竞品数据比对\zhongbiaoren.txt'
    dst_path = r'C:\Users\mayn\Desktop\公司\产品工作\竞品数据比对\urls.txt'
    url = 'https://www.jianyu360.com/jylab/bidsearchforent/index.html'

    res = set()
    lst = []

    with open(path,'r', encoding='utf8')as f:
        for line in f:
            #查看剑鱼搜索结果
            keyword = line
            print('正在爬取关键词：{}'.format(keyword))
            url_list = get_zbqy_gg_result(url, keyword)
            while (not url_list):
                url_list = get_zbqy_gg_result(url, keyword)
            if url_list == -1:
                continue
            url_list = [x.split('/')[2] for x in url_list]
            # res = res | set(url_list)
            lst = set(url_list)
            print(lst)
            with open(dst_path, 'a+', encoding='utf8')as ff:
                for u in lst:
                    # print(u)
                    ff.write(u)
                    ff.write('\n')
            # print(set(url_list))
    print(res)