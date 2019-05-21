import unittest


class FirstCase02(unittest.TestCase):
    @classmethod

    '''
    def setUpClass(self)也可
    后续研究python
    '''

    def setUpClass(cls):
        print("所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls):
        print("所有case执行之后的后置")

    def setUp(self):
        print("这个是case的前置条件")

    def tearDown(self):
        print("这个是case的后置条件")

    '''
    用例的跳转选取
    '''

    @unittest.skip("不执行第一条")
    def testfirst001(self):
        print("这个是第一条case")

    def testfirst002(self):
        print("这个是第二条case")

    def testfirst003(self):
        print("这个是第三条case")

if __name__ == "__main__":
    unittest.main()
    suite = unittest.TestSuite()
    '''
    执行顺序按照testfirst添加顺序排序
    '''
    suite.addTest(FirstCase02("testfirst002"))
    suite.addTest(FirstCase02("testfirst001"))
    suite.addTest(FirstCase02("testfirst003"))
    unittest.TextTestRunner().run(suite)
