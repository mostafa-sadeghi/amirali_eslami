# assert sum([1, 2, 2]) == 6, 'some thing happend'

# def test_sum():
#     assert sum([1, 2, 3]) == 6, "Should be 6"


# def test_sum_tuple():
#     assert sum((1, 2, 2)) == 6, "Should be 6"


# if __name__ == "__main__":
#     test_sum()
#     test_sum_tuple()
#     print("Everything passed")

# import unittest


# class TestSum(unittest.TestCase):

#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


# if __name__ == '__main__':
#     unittest.main()
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"


def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
