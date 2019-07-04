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

spilit = '|'
with open('./datafile/jibie.txt', 'r',encoding='utf-8')as f:
    for line in f:
        print(line)
        if line.strip() == '特级':
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 1))
                ff.write('\n')
        if line.strip() == '甲级' or line.strip() == '一级' :
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 2))
                ff.write('\n')
        if line.strip() == '甲级及以上':
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 3))
                ff.write('\n')
        if line.strip() == '甲级及以下':
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 4))
                ff.write('\n')
        if line.strip() == '甲级限':
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 5))
                ff.write('\n')
        if line.strip() == '乙级' or line.strip() == '二级' :
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 6))
                ff.write('\n')
        if line.strip() == '乙级及以上':
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 7))
                ff.write('\n')
        if line.strip() == '乙级及以下':
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 8))
                ff.write('\n')
        if line.strip() == '乙级限':
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 9))
                ff.write('\n')
        if line.strip() == '丙级' or line.strip() == '三级' :
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 10))
                ff.write('\n')
        if line.strip() == '丙级及以上':
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 11))
                ff.write('\n')
        if line.strip() == '丙级及以下':
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 12))
                ff.write('\n')
        if line.strip() == '丙级限':
            with open('./datafile/jibie_result.txt', 'a+',encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, 13))
                ff.write('\n')
        else:
            with open('./datafile/jibie_result.txt', 'a+', encoding='utf-8')as ff:
                ff.write('{}{}{}'.format(line.strip(), spilit, ''))
                ff.write('\n')