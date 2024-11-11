import unittest

from main import adder
class AdderTester(unittest.TestCase):
    def test_add(self):
        result = adder(1, 6)
        self.AssertEqual(result, 7)

        result = adder(11, 0)
        self.AssertEqual(result, 11)

        result = adder(-1, 0)
        self.AssertEqual(result, -1)

        result = adder(-1, -6)
        self.AssertEqual(result, -7)



