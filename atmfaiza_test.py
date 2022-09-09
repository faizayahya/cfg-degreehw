import unittest
from atmfaiza import balance
from atmtesting import atmfaiza

class MyTestCase(unittest.TestCase):
    def test_atm_balance_test(self):
        expected = 100
        result = balance(num=100)
        self.assertEqual(result, 100)

    def test_pin_number(self):
            expected = 4444
            result = balance(num=4444)
            self.assertEqual(expected, result)

    def test_maximum_withdrawal(self):
            result = withdrawal(100)
            self.assertEqual(result, balance(0), None)


if __name__ == '__main__':
    unittest.main()
