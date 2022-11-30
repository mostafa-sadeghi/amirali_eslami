import unittest


def only_odd_digits(n=0):
    string_val_of_n = str(n)
    for s in string_val_of_n:
        if int(s) % 2 == 0:
            return False
    return True


class TestOnlyOddDigits(unittest.TestCase):
    def test_is_only_digits(self):
        self.assertEqual(only_odd_digits(8), False)
        self.assertEqual(only_odd_digits(1357975313579), True)
        self.assertEqual(only_odd_digits(42), False)
        self.assertEqual(only_odd_digits(71358), False)
        self.assertEqual(only_odd_digits(0), False)
        self.assertEqual(only_odd_digits(), False)


unittest.main()
