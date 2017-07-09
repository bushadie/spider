# -*- coding:utf-8 -*-
from selenium import webdriver

# import time

driver = webdriver.Chrome()
# driver.get('http://www.baidu.com/')
# print 'open baidu'
#
# time.sleep(2)
# print 'sleep'

driver.get('http://www.bilibili.com/')  # open page
print 'open bilibili'

# driver.refresh()  # F5
# print '刷新'


driver.find_element_by_link_text(u"登录").click()  # login
print '登入'

# driver.back()
# print '后退'
#
# driver.forward()
# print '前进'

driver.find_element_by_id('login-username').send_keys('123456');
print '输入账号'

driver.find_element_by_class_name('btn-login').click()
print '登入'

driver.get("http://www.youdao.com")
driver.find_element_by_id('translateContent').send_keys('hello')
print '输入数据'
driver.find_element_by_id('translateContent').submit()
print '提交'
# submit可以和click互换
# driver.quit()
