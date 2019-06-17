import sys
# sys.path.append("F:\\Projects\\Projects\\Mooc_TestProject")
# 引入项目工程路径
# import traceback
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
import time
from log.user_log import UserLog


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.logger.info("this is Chrome")
        self.login = RegisterBusiness(self.driver)
    def tearDown(self):
        time.sleep(2)
        '''
        python2用法
        if sys.exc_info()[0]:
            self.driver.save_screenshot()
        '''
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = "F:\\report\\" + case_name + ".png"
                self.driver.save_screenshot(file_path)
        self.driver.close()
        # print("这个是case的后置条件\n")
        # self.driver.save_screenshot()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()


    # 邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
    def test_login_email_error(self):

        email_error = self.login.login_email_error("34", "111", "SS111", "test11")
        self.assertFalse(email_error)
        # if email_error == True:
        #     print("注册成功，此条case执行失败")
        # 通过assert判断是否为error

    def test_login_username_error(self):
        username_error = self.login.login_name_error("34@qq.com", "111", "SS111", "test11")
        self.assertFalse(username_error)
        # if username_error == True:
        #     print("注册成功，此条case执行失败")

    def test_login_password_error(self):
        password_error = self.login.login_password_error("34", "111", "SS111", "test11")
        self.assertTrue(password_error)
        # if password_error == True:
        #     print("注册成功，此条case执行失败")

    def test_login_code_error(self):
        code_error = self.login.login_code_error("34", "111", "SS111", "test11")
        self.assertFalse(code_error)
        # if code_error == True:
        #     print("注册成功，此条case执行失败")


    # def test_login_success(self):
    #     success = self.login.user_base("34", "111", "SS111", "test11")
    #     self.assertTrue(success)
    #     # if self.login.register_success() == True:
    #     #     print("注册成功")

# 实例化
# def main():
#     first = FirstCase
#     first.test_login_code_error()
#     first.test_login_email_error()
#     first.test_login_password_error()
#     first.test_login_username_error()
#     first.test_login_success()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(FirstCase("test_login_email_error"))
    suite.addTest(FirstCase("test_login_username_error"))
    suite.addTest(FirstCase("test_login_password_error"))
    suite.addTest(FirstCase("test_login_code_error"))
    # 所有Windows下的文件路径，一律用双反斜杠
    file_path = "F:\\report\\first_case.html"
    with open(file_path, "wb") as fp:
    # unittest.TextTestRunner().run(suite)
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="This is first report", description=u"这是我们第一次测试报告", verbosity=2)
        runner.run(suite)



