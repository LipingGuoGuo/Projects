# coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver.get("http://www.5itest.cn/register")
time.sleep(5)
# 使用title_contains检查页面是否正确
print(EC.title_contains("注册"))
email_element = driver.find_element_by_id("register_email")


element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME, "controls")
'''
使用Excepted_conditions判断元素是否可见
element = driver.find_element_by_class_name("controls")
EC.visibility_of_element_located(element) 判断传入的元素是否可见
'''
WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))
'''
输入注册用户名及获取用户信息
get_attribute()获取用户属性
'''
email_element = driver.find_element_by_id("register_email")
print(email_element.get_attribute("placeholder"))
email_element.send_keys("test123@163.com")
print(email_element.get_attribute("value"))
driver.close()

# driver.find_element_by_id("register_email").send_keys("glp123@163.com")
# # 子父节点定位  find_elements_by_class_name
# user_name_element_node = driver.find_elements_by_class_name("controls")[1]
# user_element = user_name_element_node.find_element_by_class_name("form-control")
# user_element.send_keys("glp123")
# driver.find_element_by_name("password").send_keys("11111111")
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("1111")
# driver.close()