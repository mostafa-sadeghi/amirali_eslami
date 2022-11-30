import unittest


def domino_cycle(tiles):
    new_list = []
    if len(tiles) == 0:
        return True
    for tile in tiles:
        new_list.append(tile[0])
        new_list.append(tile[1])
    if new_list[0] != new_list[-1]:
        return False
    middle_numbers = new_list[1:-1]
    for i in range(0, len(middle_numbers), 2):
        if middle_numbers[i] != middle_numbers[i+1]:
            return False
    return True


class TestDominoCycle(unittest.TestCase):
    def test_is_domino_cycle(self):
        self.assertEqual(domino_cycle([(3, 5), (5, 2), (2, 3)]), True)
        self.assertEqual(domino_cycle([(4, 4)]), True)
        self.assertEqual(domino_cycle([]), True)
        self.assertEqual(domino_cycle([(2, 6)]), False)
        self.assertEqual(domino_cycle([(5, 2), (2, 3), (4, 5)]), False)
        self.assertEqual(domino_cycle([(4, 3), (3, 1)]), False)


unittest.main()
