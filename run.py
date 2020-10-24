
from python_class import lesson_7  #导入函数文件
from test_data import test_data   #导入测试数据
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10) #隐式等待
#调用函数 先取值，再传参到函数中调用。通过key取到value值
url=test_data.url["url"]      #取值url
user=test_data.login_data['username'] #取值用户名
pwd=test_data.login_data['password']  #取值密码
s_key=test_data.s_key['s_key']   #取值搜索关键字
print(url,user,pwd,s_key)
#函数调用、传参
#返回值

result=lesson_7.search_key(driver=driver,url=url,username=user,password=pwd,s_key=s_key)
if s_key in result:
    print("搜素结果正确！")
else:
    print("测试用例不通过！")