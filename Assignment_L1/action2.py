# @Author       : Wang, Qing
# @Time         : 2021/1/31
# @Name         : action2
# @Version      : 
# @Description  : Lesson 1, action 2

"""
统计全班的成绩
班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
"""

import pandas as pd
from collections import namedtuple

# 1. 用Python来统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
Student = namedtuple('Student', ['Name', 'Chinses', 'Math', 'English'])
Course = namedtuple('Course', ['Course', 'Mean', 'Min', 'Max', 'Var', 'Std'])

zhangfei = Student('Zhang Fei', 68, 65, 30)
guanyu = Student('Guan Yu', 95, 76, 98)
liubei = Student('Liu Bei', 98, 86, 88)
dianwei = Student('Dian Wei', 90, 88, 77)
xuchu = Student('Xu Chu', 80, 90, 90)

data_score = {
    'Chinses': {},
    'Math': {},
    'English': {}
}
for stu in [zhangfei, guanyu, liubei, dianwei, xuchu]:
    data_score['Chinses'][stu.Name] = stu.Chinses
    data_score['Math'][stu.Name] = stu.Math
    data_score['English'][stu.Name] = stu.English

df_score = pd.DataFrame(data_score)
print(df_score)
"""
           Chinses  Math  English
Dian Wei        90    88       77
Guan Yu         95    76       98
Liu Bei         98    86       88
Xu Chu          80    90       90
Zhang Fei       68    65       30
"""

for course in ['Chinses', 'Math', 'English']:
    df_course = df_score[course].agg(['mean', 'min', 'max', 'var', 'std'])
    print(df_course)

"""
mean     86.200000
min      68.000000
max      98.000000
var     150.200000
std      12.255611
Name: Chinses, dtype: float64
mean     81.000000
min      65.000000
max      90.000000
var     109.000000
std      10.440307
Name: Math, dtype: float64
mean     76.600000
min      30.000000
max      98.000000
var     734.800000
std      27.107195
Name: English, dtype: float64
"""

# 2. 然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
df_score['Sum'] = df_score.sum(axis=1)
df_score.sort_values(by=['Sum'], ascending=False, inplace=True)
print(df_score)

"""
           Chinses  Math  English  Sum
Liu Bei         98    86       88  272
Guan Yu         95    76       98  269
Xu Chu          80    90       90  260
Dian Wei        90    88       77  255
Zhang Fei       68    65       30  163
"""
