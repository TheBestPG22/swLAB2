import unittest

from main import Add_num
class AdderTester(unittest.TestCase):

    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.calc = Add_num()

    def test_add(self):
        result =  self.calc.adder(self, 1 , 6)
        self.assertEqual(result, 7)

        result =  self.calc.adder(self , 11 , 0)
        self.assertEqual(result, 11)

        result =  self.calc.adder(self , -1 , 0)
        self.assertEqual(result, -1)

        result =  self.calc.adder(self , -1 , -6)
        self.assertEqual(result, -7)



