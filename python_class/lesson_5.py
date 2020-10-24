'''
import selenium 工具里的所有内容都导入
from selenium import webdriver      #从selenium工具里 导入webdriver库
driver = webdriver.Chrome()
1、打开一个网址
driver.get()
2、窗口最大化
driver.m
3、等待打开网页
time.sleep(2)
driver.get()
4、向前 向后 刷新
driver.back()
driver.forward()
driver.refresh()
5、关闭
driver.quit()    #关闭驱动，session关闭
driver.close()   #关闭当前窗口，session不会退出
'''


'''
代码     翻译（中间人）       浏览器
Python   浏览器驱动           chrome
selenium :Python 的工具，三个部分
1）ide :录制脚本
2）webdriver：库  提供网页的各种操作 + 综合语言使用 -- Python  java
3)grid：分布式

基础知识：web页面
html:标签语言  <标签头>值</标签尾>
CSS:页面布局设置，字体颜色，字体大小样式
JS:依据不同效果

元素特征：根据页面设计规则
ID:类比身份证号  ==仅限于当前页面
PS：如果不是固定的，则不能通过ID定位

对页面进行对应操作：
1、点击 click
2、传值 send_keys
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_("username").send_keys("test123")

'''
# 作业
# 代码点击登录按钮，找到


# driver.get("http://120.78.128.25:8765/")
# driver.maximize_window()
# time.sleep(2)
# driver.back()
# driver.forward()
# driver.refresh()
# driver.close()

import selenium
from selenium import webdriver
driver = webdriver.Chrome()
import time

# driver.get("http://erp.lemfix.com")
# driver.maximize_window()
# driver.find_element_by_id("username").send_keys('test123')
# time.sleep(2)
# driver.find_element_by_id("password").send_keys('123456')
# time.sleep(2)
# driver.find_element_by_id("btnSubmit").click()

driver.get("http://erp.lemfix.com")
page_text = driver.find_element_by_xpath('//div[@class="login-logo"]//b').text   #层级定位，找到定位元素的文本信息，赋值给一个变量即可
print(page_text)
page1_text =driver.find_element_by_xpath('//b[text()="柠檬ERP"]').text           #文本属性定位
print(page1_text)
page2_text= driver.find_element_by_xpath('//b[contains(text(),"柠檬")]').text     #包含属性值定位
driver.find_element_by_xpath('//input[@id="username"]').send_keys('test123')         #xpath 的表达方式
driver.find_element_by_xpath('//input[@id="password"]').send_keys('123456')
driver.find_element_by_id("btnSubmit").click()
driver.maximize_window()
page_title=driver.title                                #通过title定位
print("这个页面的标题是：{}".format(page_title))
if page2_text =="柠檬ERP":
    print("这个页面的标题是：{}".format(page_text))
else:
    print("这条测试用例不通过！")
driver.implicitly_wait(10)
login_user = driver.find_element_by_xpath('//p[text()="测试用户"]').text
print(login_user)
if login_user =="测试用户":
    print("这个登录的用户是：{}".format(login_user))
else:
    print("这条测试用例不通过！")
    #点击零售出库
driver.find_element_by_xpath('//span[text()="零售出库"]').click()
#点击搜索输入
# driver.find_element_by_xpath('//span[@class="l-btn-text icon-search l-btn-icon-left"]').click()
# driver.find_element_by_xpath('//li[@id=" "]')
# driver.switch_to.iframe('tabpanel-3fa688e472-frame')
F_id=driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")#
T_id=F_id +"-iframe"
print(T_id)

# 三种切换方式：
# 1、通过ID进行的iframe切换
driver.switch_to.frame(T_id)
driver.find_element_by_id("searchNumber").send_keys('314')
#2、通过元素定位(xpath)进行切换iframe
driver.switch_to.frame(driver.find_element_by_xpath('[@iframe={}'.format(T_id)))
driver.find_element_by_id("searchNumber").send_keys('314')
#3、通过iframe 的下标来切换
driver.switch_to.frame(1)
driver.find_element_by_id("searchNumber").send_keys('314')
#点击搜素按钮



