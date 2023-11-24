import unittest
from golden_master import GoldenMaster
from test_golden_master import TestGoldenMaster
from test_same_master import TestSameGoldenMaster
from test_trivia_refactored import TestGameRefactored

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestGoldenMaster))
    test_suite.addTest(unittest.makeSuite(TestSameGoldenMaster))
    test_suite.addTest(unittest.makeSuite(TestGameRefactored))
    return test_suite

if __name__ == '__main__':
    testSuit=suite()
    runner=unittest.TextTestRunner()
    runner.run(testSuit)