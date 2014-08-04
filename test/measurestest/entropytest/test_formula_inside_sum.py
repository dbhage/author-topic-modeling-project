'''
Created on Jul 31, 2014

@author: dbhage
'''

import unittest

from measures.entropy import formula_inside_sum

class TestFormulaInsideSum(unittest.TestCase):

    def test_case1(self):
        '''
        TC1: Invalid case. nh==-1, n==1
        '''
        nh = -1
        n = 1
        self.assertRaises(ValueError, formula_inside_sum, nh, n)

    def test_case2(self):
        '''
        TC2: Invalid case. nh==2, n==0
        '''
        nh = 2
        n = 0
        self.assertRaises(ValueError, formula_inside_sum, nh, n)
    
    def test_case3(self):
        '''
        TC3: Invalid case. nh==-10, n==3
        '''
        nh = -10
        n = 3
        self.assertRaises(ValueError, formula_inside_sum, nh, n)

    def test_case4(self):
        '''
        TC4: Invalid case. nh==3, n==-1
        '''
        nh = -10
        n = 3
        self.assertRaises(ValueError, formula_inside_sum, nh, n)

    def test_case5(self):
        '''
        TC5: Invalid case. nh==2, n==1
        '''
        nh = 2
        n = 1
        self.assertRaises(ValueError, formula_inside_sum, nh, n)

    def test_case6(self):
        '''
        TC6: Valid case. nh==8, n==50
        '''
        nh = 8
        n = 50
        actual = formula_inside_sum(nh, n)
        expected = -.293213
        self.assertAlmostEqual(actual, expected, 6, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case7(self):
        '''
        TC7: Valid case. nh==1, n==1
        '''
        nh = 1
        n = 1
        actual = formula_inside_sum(nh, n)
        expected = 0
        self.assertEqual(actual, expected, "Expected: " + str(expected) + " Actual: " + str(actual))

    def test_case8(self):
        '''
        TC8: invalid case. nh==1, n==0, should give a math domain error
        '''
        nh = 1
        n = 0
        self.assertRaises(ValueError, formula_inside_sum, nh, n)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case1']
    unittest.main()