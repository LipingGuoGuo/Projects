# coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()

driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
# 使用title_contains检查页面是否正确
print(EC.title_contains("注册"))
# email_element = driver.find_element_by_id("register_email]")
driver.save_screenshot("F:/imooc.png")
target = driver.find_element_by_xpath("//*[@id='getcode_num']")
driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

code_element = driver.find_element_by_xpath("//*[@id='getcode_num']")
# print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
im = Image.open("F:/imooc.png")
img = im.crop((left, top, right, height))
print(left, top, right, height)
img.save("F:/imooc1.png")

r = ShowapiRequest("http://route.showapi.com/184-5", "96517", "213a7970dd72492aaaee595c9d64f7d9" )
r.addBodyPara("img_base64", "data:image/jpeg;base64,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")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"F:/imooc1.png")  # 文件上传时设置
res = r.post()
text = res.json()["showapi_res_body"]["Result"]
# print(text)  # 返回信息
driver.find_element_by_id("captcha_code").send_keys(text)
time.sleep(2)


# for i in range(5):
#     user_email = ''.join(random.sample("1234567890abcdefg", 5)) + '@163.com'
#     print(user_email)

# element = driver.find_element_by_class_name("controls")
# locator = (By.CLASS_NAME, "controls")
'''
使用Excepted_conditions判断元素是否可见
element = driver.find_element_by_class_name("controls")
EC.visibility_of_element_located(element) 判断传入的元素是否可见
'''
# WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))
'''
输入注册用户名及获取用户信息
get_attribute()获取用户属性
'''
# email_element = driver.find_element_by_id("register_email")
# print(email_element.get_attribute("placeholder"))
# email_element.send_keys("test123@163.com")
# # print(email_element.get_attribute("value"))
# time.sleep(5)
# driver.close()

driver.find_element_by_id("register_email").send_keys("glp123@163.com")
# 子父节点定位  find_elements_by_class_name
user_name_element_node = driver.find_elements_by_class_name("controls")[1]
user_element = user_name_element_node.find_element_by_class_name("form-control")
user_element.send_keys("glp123")
driver.find_element_by_name("password").send_keys("11111111")
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("1111")
time.sleep(5)
driver.close()