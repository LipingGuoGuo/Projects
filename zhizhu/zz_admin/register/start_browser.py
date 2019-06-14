from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.zz-w.cn/admin/#/")
driver.maximize_window()
time.sleep(2)

element = driver.find_element_by_class_name("el-form")
locator = (By.CLASS_NAME, "el-form")
# EC 判断传入的元素是否可见
WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))
user_name_element_node = driver.find_elements_by_class_name("el-form")[0]
user_name = user_name_element_node.find_element_by_class_name("el-input__inner").send_keys("grp123")
user_password = driver.find_element_by_xpath("//*[@id='app']/div/section/main/div/form/div[2]/input").send_keys("glpglp123")
login = driver.find_element_by_xpath("//*[@id='app']/div/section/main/div/form/button/span").click()

# user_name = driver.find_element_by_xpath("//*[@id='app']/div/section/main/div/form/div[1]/input").send_keys("grp123")
# user_password = driver.find_element_by_xpath("//*[@id='app']/div/section/main/div/form/div[2]/input").send_keys("glpglp123")
# login = driver.find_element_by_xpath("//*[@id='app']/div/section/main/div/form/button/span").click()

time.sleep(3)
driver.close()