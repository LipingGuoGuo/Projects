import unittest
import os
class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path = os.path.join(os.getcwd(), "case")
        # case_path = 'F:/Projects/Projects/Mooc_TestProject/case'
        suite = unittest.defaultTestLoader.discover(case_path, pattern="unittest_*.py")
        unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    unittest.main()