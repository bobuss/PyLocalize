import unittest
from localize.app import PyLocalize

class TestApplication(unittest.TestCase):
    pass


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestApplication))

if __name__ == "__main__":
    unittest.main()
