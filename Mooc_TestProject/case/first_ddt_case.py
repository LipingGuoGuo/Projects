import ddt
import sys
sys.path.append("F:\Projects\Projects\Mooc_TestProject")
# 引入项目工程路径
import traceback
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
from util.excel_util import ExcelUtil
import os
import time

ex = ExcelUtil()
data = ex.get_data()
print(data)

@ddt.ddt
# 邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        '''
        python2中用法
        if sys.exc_info()[0]:
            self.driver.save_screenshot()
        '''
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = "F:\\report\\" + case_name + ".png"
                # file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
        # print("这个是case的后置条件")

    '''
    @ddt.data(
        ["12.com", "glp", "11111111", "code", "user_email_error", "请输入正确的邮箱地址"],
        ["@qq.com", "glp", "11111111", "code", "user_email_error", "请输入正确的邮箱地址"],
        ["12@qq.com", "glp", "11111111", "code", "user_email_error", "请输入正确的邮箱地址"]
        )

    @ddt.unpack
    '''

    @ddt.data(*data)
    def test_register_case(self,data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.login.register_function(email, username,password,code,assertCode,assertText)
        # print(email_error)
        self.assertFalse(email_error, "测试失败")

if __name__ == "first_ddt_data":
    # file_path = os.path.join(os.getcwd() + "/report/" + "first_case1.html")
    # f = open(file_path, "wb")
    # suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report1", description=u"这是我们第一次测试报告1", verbosity=2)
    # runner.run(suite)
    # 所有Windows下的文件路径，一律用双反斜杠
    file_path = "F:\\report\\first_case1.html"
    with open(file_path, "wb") as fp:
        # unittest.TextTestRunner().run(suite)
        suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="This is first report", description=u"这是我们第一次测试报告1",
                                               verbosity=2)
        runner.run(suite)