''''''
'''
代码     翻译（中间人）       浏览器
Python   浏览器驱动           chrome
selenium :Python 的工具，三个部分
1）ide :录制脚本
2）webdriver：库  提供网页的各种操作 + 综合语言使用 -- Python  java
3)grid：分布式

基础知识：
web页面包含
html:标签语言  <标签头>值</标签尾>
CSS:页面布局设置，字体颜色，字体大小样式
JS:依据不同效果

元素特征：根据页面设计规则 ID:类比身份证号  ==仅限于当前页面  （PS：如果不是固定的，则不能通过ID定位）
八大元素定位方式：id/name/xpath/css/class/tag/link/partial_link
xpath的元素定位方式：
1、绝对路径（右键COPY）顺序不稳定不安全/相对路径
xpath的表达方式：属性名+属性值  xpath("//标签名[@属性名='属性值']")driver.find_element_by_xpath('//input[@id="username"]')
2、层级定位 xpath("//标签名[@属性名='属性值']//下一级标签名") driver.find_element_by_xpath('//div[@class="login-logo"]//b')
3、文本定位 xpath("//标签名[text（）='文本值']")           driver.find_element_by_xpath('//b[text()="柠檬ERP"]')
4、包含定位 "//标签名[contains（@属性名/text(),属性值)]"  driver.find_element_by_xpath('//b[contains(text(),"柠檬")]')
Python对页面可实现的四大操作：
1、点击 click
driver.find_element_by_id("btnSubmit").click()
2、传值 send_keys
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_name("username").send_keys("test123")
3、获取文本：text()
page_text = driver.find_element_by_xpath('//div[@class="login-logo"]//b').text 获取文本信息赋值给一个变量
4、获取属性：get_attribute()
三种等待方式
强制等待  time.sleep(5) ====== 没有完成等待时间，不往下执行
智能等待
隐式等待：可以设置等待时间，在等待时间没有结束之前，元素找到了就不再等待，继续往下执行    driver.implicitly_wait(10), 一个session里面只执行一次
显示等待：expected_condition （） PS：指定特定条件 确定等待时间   Python 班级

页面层级中如果出现iframe，需进行iframeq切换，才可以对元素进行定位
# driver.find_element_by_xpath('//input[@id="searchNumber"]').send_keys("314") #该条代码无法定位传值原因HTML嵌套,需进行iframe切换
iframe 三种切换方式：（元素唯一）
1、通过ID进行的iframe切换
driver.switch_to.frame(T_id)  #通过id切换
driver.find_element_by_id("searchNumber").send_keys('314')
driver.find_element_by_xpath('//span[@class="l-btn-left"]').click()
2、通过元素定位(xpath)进行切换iframe  #通过xpath定位 (如果id不固定，不能用id定位）
driver.switch_to.frame("driver.find_element_by_xpath('//iframe[@id={}'.format(T_id))) #通过元素定位(xpath)进行切换
driver.find_element_by_id("searchNumber").send_keys('314')
driver.find_element_by_xpath('//span[@class="l-btn-left"]').click()
3、通过iframe 的下标来切换
driver.switch_to.frame(1)
driver.find_element_by_id("searchNumber").send_keys('314')
driver.find_element_by_xpath('//span[@class="l-btn-left"]').click()
tagname = 
web自动化测试覆盖两种：冒烟测试、回归测试
实现正常核心功能，冒烟测试居多；回归测试 用例覆盖里较高
针对重复使用，值不固定的可以封装为函数，如用户名密码，定义函数
def
自动化测试的成熟框架结构：
公共方法/函数 python_class
测试数据    test_data
日志报告    test_result
启动文件    run.py


'''

#函数调用
import time
def login_page(username,password,driver):#传入参数，形参
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()
def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    F_id=driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
    T_id=F_id+'-frame'
    driver.switch_to.frame(T_id)
    driver.find_element_by_id("searchNumber").send_keys(s_key) #搜索单据编号，传入编号值 314
    driver.find_element_by_xpath('//a[@id="searchBtn"]').click()#点击查询按钮  根据按钮定位
    time.sleep(1)           #隐式等待与强制等待可结合使用
    num=driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    #点击查询后页面出现一行的值，如果不搜索查询，则id按所有值的顺序显示行号
    return num


# import selenium
# from selenium import webdriver
# driver = webdriver.Chrome()
# import time
# driver.implicitly_wait(10)   #设置隐式等待
# driver.get("http://erp.lemfix.com") #打开柠檬ERP网站
# page_text=driver.find_element_by_xpath('//div[@class="login-logo"]//b').text#获取页面的标题
# print(page_text)   #输出页面标题
# page_title=driver.title           #输出页面标题的title表达方式
# if page_title == "柠檬ERP":    #验证页面标题是否与预期一致
#     print('这个页面的标题是：{}'.format(page_title)) #格式化输出
# else:
#     print('这条测试用例不通过！')
# driver.maximize_window()         #窗口最大化
#
# driver.find_element_by_xpath('//input[@id="username"]').send_keys("test123")#输入用户名
# driver.find_element_by_xpath('//input[@id="password"]').send_keys("123456")#输入密码
# driver.find_element_by_id("btnSubmit").click() #点击登录
#
# login_name=driver.find_element_by_xpath('//div[@class="pull-left info"]//p').text #获取页面的登录用户名
# if login_name=="测试用户":                                        #验证登录用户名的正确性
#     print('这个登录用户的用户名是:{}'.format(login_name))          #格式化输出
# else:
#     print('这条测试用例不通过！')            #覆盖测试用例
#
# driver.find_element_by_xpath('//span[text()="零售出库"]').click() #点击零售出库
# # tagname = driver.find_element_by_tag_name("iframe")
# # print(tagname)
# F_id=driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")#获取属性值
# T_id=F_id+'-frame'#拼接属性值
# print(T_id)
# driver.switch_to.frame(T_id)   #通过id切换
# #driver.switch_to.frame("driver.find_element_by_xpath('//iframe[@id={}'.format(T_id))) #通过xpath切换
# #driver.switch_to.frame(1)         #通过下标切换iframe
# driver.find_element_by_id("searchNumber").send_keys('314') #搜索单据编号，传入编号值 314
# driver.find_element_by_xpath('//a[@id="searchBtn"]').click()#点击查询按钮  根据按钮而非“查询”定位
# time.sleep(1)           #隐式等待与强制等待可结合使用
# num=driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text#点击查询后页面出现一行的值，如果不搜索查询，则id按所有值的顺序显示行号
# print(num)  #输出单据编号
# if "314" in num:
#     print("搜素结果正确！")
# else:
#     print("测试用例不通过！")









#练习测试重置功能
# driver.find_element_by_xpath('//span[@class="l-btn-text icon-redo l-btn-icon-left"]').click()#点击重置页面输入框未清除
#练习搜索商品信息，检查搜索结果
# driver.find_element_by_xpath('//input[@id="searchMaterial"]').send_keys("商品1")
# driver.find_element_by_xpath('//a[@id="searchBtn"]').click()
# time.sleep(1)
# name=driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="materialsList"]/div').text
# print('这个商品的名称是：{}'.format(name))
# if "商品1" in name:
#     print('搜索结果正确！')
# else:
#     print('测试用例不通过！')

