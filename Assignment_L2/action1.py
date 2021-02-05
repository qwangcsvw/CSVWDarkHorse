# -*- coding : utf-8 -*-
# @Author       : Wang, Qing
# @Time         : 2021/2/5
# @Name         : action 2
# @Version      : 
# @Description  : Lesson 2, action 2

"""
Action1：汽车投诉信息采集：
数据源：http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml
投诉编号，投诉品牌，投诉车系，投诉车型，问题简述，典型问题，投诉时间，投诉状态
可以采用Python爬虫，或者第三方可视化工具
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


def getPageContent(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
    urlHtml = requests.get(url, headers=headers, timeout=10)
    urlContent = urlHtml.text
    urlSoup = BeautifulSoup(urlContent, 'html.parser', from_encoding='utf-8')
    return urlSoup


def findInfo(soup):
    df = pd.DataFrame(columns=[
        'problemId',
        'carBrand',
        'carModel',
        'carType',
        'problemDescription',
        'problemCode',
        'problemDatetime',
        'problemStatus'
    ])

    tempInfo = soup.find('div', class_='tslb_b')
    # print(tempInfo)
    trList = tempInfo.find_all('tr')
    for tr in trList:
        tdList = tr.find_all('td')
        if len(tdList) > 0:
            problemDict = {}
            problemDict['problemId'] = tdList[0].text
            problemDict['carBrand'] = tdList[1].text
            problemDict['carModel'] = tdList[2].text
            problemDict['carType'] = tdList[3].text
            problemDict['problemDescription'] = tdList[4].text
            problemDict['problemCode'] = tdList[5].text
            problemDict['problemDatetime'] = tdList[6].text
            problemDict['problemStatus'] = tdList[7].text
            df = df.append(problemDict, ignore_index=True)
    return df


if __name__ == '__main__':
    baseUrl = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
    pageNum = 20
    resDf = pd.DataFrame(columns=[
        'problemId',
        'carBrand',
        'carModel',
        'carType',
        'problemDescription',
        'problemCodeproblemCode',
        'problemDatetime',
        'problemStatus'
    ])
    for i in range(pageNum):
        url = '{}{}.shtml'.format(baseUrl, i+1)
        soup = getPageContent(url)
        df = findInfo(soup)
        resDf = resDf.append(df, ignore_index=True)
    print(resDf)
    resDf.to_csv('L2_car_complain.csv', index=False)

