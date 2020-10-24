'''
lesson_03作业

list1 = ['方方土','七木','荷花鱼','kinggo','Amiee','焕蓝']
list2 = []
dict1 = {'name':'方方土','gender':'男','age':18,'city':'北京'}
list2.append(dict1)
dict2 = {'name':'七木','gender':'男','age':19,'city':'上海'}
list2.append(dict2)
dict3 = {'name':'荷花鱼','gender':'男','age':20,'city':'长沙'}
list2.append(dict3)
dict4 = {'name':'kinggo','gender':'女','age':21,'city':'深圳'}
list2.append(dict4)
dict5 = {'name':'Amiee','gender':'女','age':22,'city':'济南'}
list2.append(dict5)
dict6 = {'name':'焕蓝','gender':'女','age':23,'city':'青岛'}
list2.append(dict6)

for name in list2:
    print(name)
'''
'''
for循环语句：
for 变量名 in 数据对象：
    子代码（循环体）
循环次数由元素个数决定
中断：break continue
range()=内置函数  跟for循环语句一起使用 range(1,5,1) 取头不取尾

'''
'''
函数：


'''


# count=0
# list1=['tt','rr','ee','ww','qq','ii','uu','yy','oo']
# for name in list1:
#     if name == 'ee':
#         #break        #跳出整个循环
#         continue
#     print(name)
#     print("*"*20)
#     count +=1
# print(count)
# print(len(list1))
# for i in range(1,6,1):
#     print(i)
# count = 0
# list1 = ['方方土','七木','荷花鱼','kinggo','Amiee','焕蓝']
# for name in list1:
#     if name == "荷花鱼":
#         continue
#     print(name)
#     count +=1
# print(count)
# print(len(list1))
#
# for i in range(5):
#       print(i)
#
# def good_job():
#     salary = 8000
#     bonus  = 2000
#     subsidy =500
#     sum1 = salary + bonus + subsidy
#     print("这个工作的工资总和是{}".format(sum1)) #格式化输出
# good_job()
#
# def good_job(salary,bonus,subsidy):
#     print("salary:{}".format(salary))
#     print("bonus:{}".format(bonus))
#     print("subsidy:{}".format(subsidy))
#     sum1=salary+bonus+subsidy
#     print("这个工作的工资总和是：{}".format(sum1))
# good_job(8000,5000,100)
# def good_job(salary,subsidy,bonus=300,*args,**kwargs):
#     sum1=salary+bonus+subsidy
#     print("salary:{}".format(salary))
#     print("bonus:{}".format(bonus))
#     print("subsidy:{}".format(subsidy))
#     print("args：{}".format(args))
#     print("kwargs:{}".format(kwargs))
#     for i in args:
#         sum1 += i
#     for j in kwargs:
#         sum1 += kwargs[j]
#     print("这个工作的总和是：{}".format(sum1))
# good_job(8000,5000,100,10,30,aa=11,bb=12,cc=13)
# def good_job(salary,subsidy,bonus=300,*args,**kwargs):
#     sum1=salary+bonus+subsidy
#     for i in args:
#         sum1 += i
#     for j in kwargs:
#         sum1 += kwargs[j]
#     return sum1,bonus
# result = good_job(8000,5000,100,10,30,aa=11,bb=12,cc=13)
# print(result)
# if result > 10000:
#     print("这是一个不错的工作")
# else:
#     print("我可以找到更好的工作")
#
# 作业
# str = "aa","bb","cc","dd"
# list1 = list(str)
# print(list1)
# print("*"*50)
#
# sum0 = 0
# for i in range(1,10,1):
#     print(i)
#     sum0 += i
# print(sum0)
# print("*"*50)
#
#
# def object(str1,str2,**kwargs):
#     sum1=len(str1)+len(str2)+len(kwargs)
#     if sum1 > 5:
#         print('true')
#     else:
#         print('false')
#     return sum1
# result = object("qcd","lemon",aa=11,bb=12,cc=13,dd=14,ff=15)
# print(result)
# 课堂讲解版
# def add_fun(num):
#     sum = 0
# # num = int(input("正数："))
#     for i in range(num):
#         sum += i
#     print(sum)
# add_fun(100)
# def add_fun(object):
#     if type(object)==list or type(object)==dict or type(object)==str :
#         if len(object) >= 5:
#             print('true')
#         else:
#             print('false')
#
#
#     else:
#         print("这个数据类型不能计算长度")
# add_fun({"name":"key","id":"12"})