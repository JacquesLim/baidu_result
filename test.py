#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   test.py    
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/27 11:36   Jacques Lim    1.0         None
'''
import re,json
import random
import datetime
# spilit = '|'
# with open('./datafile/jstzizhi.txt', 'r',encoding='utf-8')as f:
#     text = f.read()
#     zizhi_list = json.loads(text)
#     print(zizhi_list)
#     with open('./datafile/zizhi.txt', 'a+',encoding='utf-8')as ff:
#         for zizhi in zizhi_list:
#             ff.write('{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}'.format(zizhi['CategoryID'], spilit, zizhi['CategoryName'], spilit, zizhi['ParentID'], spilit, zizhi['ProvinceIDs'], spilit, zizhi['MatchText'], spilit, zizhi['Compare'], spilit, zizhi['CompareID'], spilit, zizhi['IsExpand'], spilit, zizhi['Sort']))
#             ff.write('\n')

# print(random.randint(1,3))

today = datetime.datetime.now()
NOW = '{}_{}_{}_{}_{}'.format(today.year, today.month, today.day, today.hour, today.minute)
src = r'C:\Users\mayn\Desktop\公司\产品工作\竞品数据比对\bst_urls.txt'
dst = r'C:\Users\mayn\Desktop\公司\产品工作\竞品数据比对\urls.txt'
dif_path = r'C:\Users\mayn\Desktop\公司\产品工作\竞品数据比对\dif_{}.txt'.format(NOW)
inc_path = r'C:\Users\mayn\Desktop\公司\产品工作\竞品数据比对\inc_{}.txt'.format(NOW)

# with open(src, 'r', encoding='utf8')as f:
#     text = f.read().strip()
#     text = text.split('\n')
#     # print(text)
#     url_list = [x.split('/')[2] for x in text]
#     lst = set(url_list)
#     for url in lst:
#         with open(dst,'a+', encoding='utf8')as ff:
#             ff.write(url)
#             ff.write('\n')

dif = set()
with open(src, 'rb')as f:
    text = f.read().strip().replace(b'\r',b'')
    src_list = text.split(b'\n')
    with open(dst, 'rb')as ff:
        tt = ff.read().strip().replace(b'\r',b'')
        dst_list = tt.split(b'\n')
        src_set = set(src_list)
        dst_set = set(dst_list)
        print(src_set)
        print(dst_set)
        dif = dst_set - src_set
        for uu in dif:
            with open(dif_path, 'ab+')as fff:
                fff.write(uu)
                fff.write(b'\n')

print('dif:{}'.format(dif))
