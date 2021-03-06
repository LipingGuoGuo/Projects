"""二次封装webdriver"""

from selenium import webdriver
# from util.read_ini import ReadIni
from base.find_element import FindElement
import time

class ActionMethod:
    # def __init__(self):
    #     pass
    # 打开浏览器
    def open_browser(self):
        # if browser == "Chrome":
        self.driver = webdriver.Chrome()
        # else:
        #     self.driver = webdriver.Firefox()
        # else:
        #     self.driver = webdriver.Edge()
    # 输入地址
    def get_url(self,url):
        # self.driver.get(url)
        return 1

    # 定位元素
    def get_element(self,key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    # 输入元素
    def element_send_keys(self,value,key):
        element = self.get_element(key)
        if(element):
            element.send_keys(value)

    # 点击元素
    # def click_element(self,key):
    #     self.get_element(key).click()

    # 等待
    def sleep_time(self):
        time.sleep(5)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()

    # 获取title
    def get_title(self):
        title = self.driver.title
        return title

