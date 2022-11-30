import unittest


def is_cyclops(n):
    string_n = str(n)
    half_len = len(string_n)//2
    zero_counts = string_n.count('0')
    if string_n[half_len] != '0' or zero_counts != 1:
        return False
    return True


class TestCyclops(unittest.TestCase):
    def test_is_cyclops(self):
        self.assertEqual(is_cyclops(0), True)
        self.assertEqual(is_cyclops(101), True)
        self.assertEqual(is_cyclops(98053), True)
        self.assertEqual(is_cyclops(777888999), False)
        self.assertEqual(is_cyclops(1056), False)
        self.assertEqual(is_cyclops(675409820), False)


unittest.main()
