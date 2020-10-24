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

'''
import selenium #工具里的所有内容都导入
from selenium import webdriver      #从selenium工具里 导入webdriver库
driver = webdriver.Chrome()
import time
driver.implicitly_wait(10)          #设置隐式等待
driver.get("http://erp.lemfix.com") #打开柠檬ERP网站
page_text=driver.find_element_by_xpath('//div[@class="login-logo"]//b').text#获取页面的标题
print(page_text)   #输出页面标题
page_title=driver.title           #输出页面标题的title表达方式
if page_title == "柠檬ERP":    #验证页面标题是否与预期一致
    print('这个页面的标题是：{}'.format(page_title)) #格式化输出
else:
    print('这条测试用例不通过！')
driver.find_element_by_xpath('//input[@id="username"]').send_keys("test123")#输入用户名
driver.find_element_by_xpath('//input[@id="password"]').send_keys("123456")#输入密码
driver.find_element_by_id("btnSubmit").click() #点击登录
driver.maximize_window()         #窗口最大化
login_name=driver.find_element_by_xpath('//div[@class="pull-left info"]//p').text #获取页面的登录用户名
if login_name=="测试用户":                                        #验证登录用户名的正确性
    print('这个登录用户的用户名是:{}'.format(login_name))          #格式化输出
else:
    print('这条测试用例不通过！')
driver.find_element_by_xpath('//span[text()="零售出库"]').click() #点击零售出库
# driver.find_element_by_xpath('//input[@id="searchNumber"]').send_keys("314") #该条代码无法定位传值原因HTML嵌套
#页面层级中如果出现iframe，需进行iframeq切换，才可以对元素进行定位
#iframe元素定位方式：(如果id不固定，不用id定位）
f_iframe=driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
t_iframe=f_iframe+'-frame'
print(t_iframe)    #取出子页面的属性值
driver.switch_to.frame(t_iframe)   #切换iframe
driver.find_element_by_xpath('//input[@id="searchNumber"]').send_keys("314")  #传入单据编号值
driver.find_element_by_xpath('//span[@class="l-btn-left"]').click()           #点击查询按钮





# page_text = driver.find_element_by_xpath('//div[@class="login-logo"]//b').text   #层级定位，找到定位元素的文本信息，赋值给一个变量即可
# print(page_text)
# page1_text =driver.find_element_by_xpath('//b[text()="柠檬ERP"]').text           #文本属性定位
# print(page1_text)
# page2_text= driver.find_element_by_xpath('//b[contains(text(),"柠檬")]').text     #包含属性值定位
# driver.find_element_by_xpath('//input[@id="username"]').send_keys('test123')         #xpath 的表达方式
# driver.find_element_by_xpath('//input[@id="password"]').send_keys('123456')
# driver.find_element_by_id("btnSubmit").click()
# driver.maximize_window()
# page_title=driver.title                                #通过title定位
# print("这个页面的标题是：{}".format(page_title))
# if page2_text =="柠檬ERP":
#     print("这个页面的标题是：{}".format(page_text))
# else:
#     print("这条测试用例不通过！")
# driver.implicitly_wait(10)
# login_user = driver.find_element_by_xpath('//p[text()="测试用户"]').text
# print(login_user)
# if login_user =="测试用户":
#     print("这个登录的用户是：{}".format(login_user))
# else:
#     print("这条测试用例不通过！")
#     #点击零售出库
# driver.find_element_by_xpath('//span[text()="零售出库"]').click()
# #点击搜索输入
# # driver.find_element_by_xpath('//span[@class="l-btn-text icon-search l-btn-icon-left"]').click()
# # driver.find_element_by_xpath('//li[@id=" "]')
# # driver.switch_to.iframe('tabpanel-3fa688e472-frame')
# F_id=driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")#
# T_id=F_id +"-iframe"
# print(T_id)
#




