# @Author       : Wang, Qing
# @Time         : 2021/1/31
# @Name         : action1
# @Version      : 
# @Description  : Lesson 1, action 1

""" Action1：求2+4+6+8+...+100的求和，用Python该如何写 """

sumRes = 0
n = 2

while n <= 100:
    sumRes += n
    n += 2

print(sumRes)
