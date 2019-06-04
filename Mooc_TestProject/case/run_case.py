import unittest
# import os
class RunCase(unittest.TestCase):
    def test_case01(self):
        test_dir = "./"
        # case_path = 'F:/Projects/Projects/Mooc_TestProject/case'
        discover = unittest.defaultTestLoader.discover(test_dir, pattern="unittest_*.py")

        runner = unittest.TextTestRunner()
        runner.run(discover)

if __name__ == "__main__":
    unittest.main()