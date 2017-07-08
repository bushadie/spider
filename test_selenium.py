# -*- coding:utf-8 -*-
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')

time.sleep(2)
browser.get('http://www.bilibili.com/')  # open page
browser.refresh()  # F5
# browser.find_element_by_id('i_menu_login_btn').send_keys('123456');
browser.find_element_by_link_text(u"登录").click()  # login
