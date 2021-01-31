# @Author       : Wang, Qing
# @Time         : 2021/1/31
# @Name         : action3
# @Version      : 
# @Description  : Lesson 1, action 3

"""
对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多
"""
import os
import re
import sys
from pathlib import Path
import pandas as pd

# Step1，数据加载
pwd = Path.cwd()
csv_path = Path(pwd, 'car_complain.csv')
if not csv_path.exists():
    print('File {} does not exist!'.format(csv_path))
    sys.exit(1)

df = pd.read_csv(csv_path)
print(df)

# Step2，数据预处理
# 拆分problem类型 => 多个字段
df_problem = df.copy()
for i in range(df_problem.shape[0]):
    proList = re.split(',', df_problem.loc[i, 'problem'].strip())
    for pro in proList:
        if pro != '':
            df_problem.loc[i, pro] = 1
print(df_problem)

# Step3，数据统计
# 对数据进行探索：品牌投诉总数，车型投诉总数
# 哪个品牌的平均车型投诉最多
df_sort = df.loc[:, ['brand', 'car_model']].sort_values(by=['brand', 'car_model'], ascending=False)
df_sort.replace({'brand': {'(.*)-(.*)': r'\1\2'}}, regex=True, inplace=True)
print(df_sort)
# a. 品牌投诉总数
brand_count = df_sort.loc[:, 'brand'].value_counts()
print(brand_count)
brandList = brand_count.index
print(brandList)
# b. 车型投诉总数
carModelCount = df_sort.loc[:, 'car_model'].value_counts()
print(carModelCount)
carModelList = carModelCount.index
print(carModelList)
# c. 哪个品牌的平均车型投诉最多
# 每个品牌的平均车型投诉数量 = 品牌投诉数量 / 车型数量

avg_dict = {'brand': [],
            'average': []}
for brand in brandList:
    brandTotalNum = brand_count[brand]
    brandCarModel = df_sort.loc[df_sort['brand'] == brand, 'car_model'].value_counts().keys()
    carModelNum = len(brandCarModel)
    brand_avg = brandTotalNum / carModelNum
    avg_dict['brand'].append(brand)
    avg_dict['average'].append(brand_avg)

df_avg = pd.DataFrame(avg_dict)
df_avg.sort_values(by=['average'], ascending=False, inplace=True)
df_avg.reset_index(drop=True, inplace=True)
print(df_avg)
"""
        brand    average
0       一汽马自达  47.500000
1        吉利汽车   9.600000
2        一汽大众   8.285714
3        广汽丰田   5.666667
4        上汽大众   3.600000
5        东风日产   3.200000
6      一汽大众奥迪   3.166667
[74 rows x 2 columns]
"""
print('平均车型投诉最多的品牌是：{}'.format(df_avg.loc[0, 'brand']))

