import unittest


def count_dominators(items):
    new_list = []
    if len(items) == 0:
        return 0
    for i in range(len(items)):
        is_domin = True
        for j in range(i+1, len(items)):
            if items[i] <= items[j]:
                is_domin = False
                break
        if is_domin:
            new_list.append(items[i])
    return len(new_list)


class TestCountDominators(unittest.TestCase):
    def test_is_domin(self):
        self.assertEqual(count_dominators([42, 7, 12, 9, 2, 5]), 4)
        self.assertEqual(count_dominators([]), 0)
        self.assertEqual(count_dominators([99]), 1)
        self.assertEqual(count_dominators([42, 42, 42, 42]), 1)
        self.assertEqual(count_dominators(range(10**7)), 1)
        self.assertEqual(count_dominators(range(10**7, 0, -1)), 10000000)


unittest.main()
