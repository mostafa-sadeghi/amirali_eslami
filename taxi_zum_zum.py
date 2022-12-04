import unittest


def taxi_zum_zum(moves):

    origin = [0, 0]
    direction = 0
    for move in moves:
        if move == 'R':
            direction += 90
        if move == 'L':
            direction -= 90
        if move == 'F':
            if direction in (0, 360, -360):
                origin[1] += 1
            if direction in (90, -270):
                origin[0] += 1
            if direction in (180, -180):
                origin[1] -= 1
            if direction in (-90, 270):
                origin[0] -= 1
    return tuple(origin)


class TestTaxiZumZum(unittest.TestCase):
    def test_taxi_zum_zum(self):
        self.assertEqual(taxi_zum_zum('RFRL'), (1, 0))
        self.assertEqual(taxi_zum_zum('LFFLF'), (-2, -1))
        self.assertEqual(taxi_zum_zum('LLFLFLRLFR'), (1, 0))
        self.assertEqual(taxi_zum_zum('FR' * 1729), (0, 1))
        self.assertEqual(taxi_zum_zum('FFLLLFRLFLRFRLRRL'), (3, 2))


unittest.main()
