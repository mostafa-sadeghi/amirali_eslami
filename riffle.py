import unittest


def riffle(items, out=True):
    length_half = len(items)//2
    new_items = []
    first_half = items[:length_half]
    second_half = items[length_half:]
    for i in range(length_half):
        if out:
            new_items.append(first_half[i])
            new_items.append(second_half[i])
        else:
            new_items.append(second_half[i])
            new_items.append(first_half[i])
    return new_items


class TestRiffle(unittest.TestCase):
    def test_riffle(self):
        self.assertEqual(riffle([1, 2, 3, 4, 5, 6, 7, 8], True), [
                         1, 5, 2, 6, 3, 7, 4, 8])
        self.assertEqual(riffle([1, 2, 3, 4, 5, 6, 7, 8], False), [
                         5, 1, 6, 2, 7, 3, 8, 4])
        self.assertEqual(riffle([], True), [])
        self.assertEqual(riffle(['bob', 'jack'], True), ['bob', 'jack'])
        self.assertEqual(riffle(['bob', 'jack'], False), ['jack', 'bob'])


unittest.main()
