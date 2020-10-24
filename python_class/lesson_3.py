'''
list1= [20,3.1415926,True,"北京",[1,2,3,4,5]]
print(type(list1))
print(list1[1:4:2])   #   打印列表
print(list1[4][2])    #   嵌套取值  打印  列表  list1中字符串的元素
#  增加
list1.append("江苏")    #   列表末尾添加 ---P1
print(list1)
list1.insert(2,'天津')   #    指定位置  元素插入----P2
print(list1)
list1.extend(['河北','山东','安徽'])    #   列表合并----P3
print(list1)
# 删除
list1.pop()         #默认删除末尾
print(list1)

list1.pop(1)         #指定 索引 删除
print(list1)

list1.remove(True)    #指定 元素 删除
print(list1)

list1.clear()        #清除所有元素
print(list1)

# 修改
list1[1]='上海'       #重新赋值
list1[4]='广州'
print(list1)

list1.append('上海')    #可以添加重复元素
print(list1)

print(len(list1))      #统计个数
print(list1.count(list1))
'''

# tuple = (20, '上海', [1, 2, 3, 4, 5], '河北', '广州','上海')
# print(tuple)
# print(tuple[3])
# print(tuple.count('上海'))
# print(len(tuple))
#
# list2 = list(tuple)     #元组转换为列表
# print(list2)
# list2[-1]= '甘肃'
# print(list2)
# tuple2 =tuple(list)     #列表转换回为元组
# print(tuple)


'''
Python 常用数据类型：列表（list)、元组、字典、控制流

list ： []  元素之间用英文逗号隔开
1、元素：任意数据类型，int/float/bool/str/list....
2、取值：类比字符串  通过索引取值
3、列表元素可以被改变：增  删   改
4、元素可以重复  统计元素个数  len() list.count('元素'）
元组 tuple:()
1、元素：任意数据类型，int/float/bool/str/list....
2、取值：类比字符串  通过索引取值
3、列表元素不可以被改变：增  删   改  元组不可以赋值
4、元素可以重复  统计元素个数  len() tuple.count('元素'）
5、list  tuple 可以转换

字典 dict {}
1、元素：    key (类似EXCEL的表头) :value(键值对)   json
2、场景：    存储数据属性
key  1）不能是改变的数据类型 可以是字符串
     2）不能重复  唯一
value:可以是任意数据类型   可以改变  增删改
3、字典没有顺序 不存在索引
4、len()--------长度
集合：set {} 
1、无序
2、元素不可重复
'''

#取值
#dict1={"name":"tan","height":"180","weight":"160"}
# print(dict1['height'])
# print(dict1.get('weight'))     #取值方式两种   dict1[]   dict1.get()
#增加
# dict1['weight']='150'     #Kkey存在，赋值为修改，key不存在 ，赋值为增加
# print(dict1)
# dict1['age']='18'
# print(dict1)
# dict1.update({"gender":"男","city":"北京","hobby":"学习"})   #类比有extend功能
# print(dict1)
# #删除
# dict1.pop('age')    #指定key删除对应的键值对
# print(dict1)
# del dict1           #变量存储删除对象不存在
# print(dict1)
# list1=["11","22","33","11","44"]
# set1 = set(list1)
# print(set1)
# a = [1,2,'6','summer']
# print('i'  in  a)
#
# if 'i' in a:
#     print('i是a的成员')
# else:
#     print('不是')
# dict1 ={"class_id":45,'num':20}
# if dict1['num'] > 5:
#     print(dict1['num'])
dict1 ={"class_id":45,'num':20}
num = dict1.get("num")
if num >5:
    print('班上人数是：{}'.format(num))
else:
    print('班上人数不足5人！')

# list1 = ['方方土','七木','荷花鱼','kinggo','Amiee','焕蓝']
# list2 = []
# dict1 = {'name':'方方土','gender':'男','age':18,'city':'北京'}
# list2.append(dict1)
# dict2 = {'name':'七木','gender':'男','age':19,'city':'上海'}
# list2.append(dict2)
# dict3 = {'name':'荷花鱼','gender':'男','age':20,'city':'长沙'}
# list2.append(dict3)
# dict4 = {'name':'kinggo','gender':'女','age':21,'city':'深圳'}
# list2.append(dict4)
# dict5 = {'name':'Amiee','gender':'女','age':22,'city':'济南'}
# list2.append(dict5)
# dict6 = {'name':'焕蓝','gender':'女','age':23,'city':'青岛'}
# list2.append(dict6)
# print(list2)
#
#
# print('*'*100)
# #自动
# for name in list2:
#     print(name)
#

list1 = ['方方土','七木','荷花鱼','kinggo','Amiee','焕蓝']
dict1 = {'name':'方方土','gender':'男','age':18,'city':'北京'}
dict2 = {'name':'七木','gender':'男','age':19,'city':'上海'}
dict3 = {'name':'荷花鱼','gender':'男','age':20,'city':'长沙'}
dict4 = {'name':'kinggo','gender':'女','age':21,'city':'深圳'}
dict5 = {'name':'Amiee','gender':'女','age':22,'city':'济南'}
dict6 = {'name':'焕蓝','gender':'女','age':23,'city':'青岛'}
list2 = [dict1,dict2,dict3,dict4,dict5,dict6]
print(list2)

list0 = []
list1 = ['方方土','七木','荷花鱼','kinggo','Amiee','焕蓝']
list2 = [18,19,20,21,22,23]
list3 = ['男','男','男','女','女','女']
list4 = ['北京','上海','长沙','深圳','济南','青岛']
for i in range(6):
    dict1=dict(name=list1[i],age=list2[i],gender=list3[i],city=list4[i])
    list0.append(dict1)
print(list0)




