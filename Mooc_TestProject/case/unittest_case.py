"""
不可命名为unittest,否则会报错
case 必须以test开始
unittest用例执行顺序按照添加的数字升序排列
"""
import unittest
class FirstCase01(unittest.TestCase):
    # 装饰器
    @classmethod
    def setUpClass(cls):
        print("所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls):
        print("所有case执行之后的后置")

    def setUp(self):
        print("这个是case的前置条件")

    def tearDown(self):
        print("这个是case的后置条件\n")

    @unittest.skip("不执行第一条")
    def testfirst01(self):
        print("这个是第一条case")

    def testfirst02(self):
        print("这个是第二条case")

    def testfirst03(self):
        print("这个是第三条case")

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    '''
    执行顺序按照testfirst添加顺序排序
    '''
    suite.addTest(FirstCase01("testfirst02"))
    suite.addTest(FirstCase01("testfirst01"))
    suite.addTest(FirstCase01("testfirst03"))
    unittest.TextTestRunner().run(suite)

