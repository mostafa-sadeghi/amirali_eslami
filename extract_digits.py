import unittest


def extract_increasing(digits):
    output = [int(digits[0])]
    prev = 1
    status = True
    while status:
        for current in range(prev+1, len(digits)):
            number = int(digits[prev:current])
            if number > output[-1]:
                output.append(number)
                prev = current
        else:
            status = False
    return (output, len(output), str(output[-1]))


class TestExtractIncreasing(unittest.TestCase):
    def test_extract_increasing(self):
        self.assertEqual(extract_increasing('600005')[0], [6])
        self.assertEqual(extract_increasing('045349')[0], [0, 4, 5, 34])
        self.assertEqual(extract_increasing(
            '77777777777777777777777')[0], [7, 77, 777, 7777, 77777, 777777])
        self.assertEqual(extract_increasing(
            '2718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260')[0], [2, 7, 18, 28, 182, 845, 904, 5235,
                                                                                                                                                                            36028, 74713, 526624, 977572, 4709369,
                                                                                                                                                                            9959574, 96696762, 772407663, 3535475945,
                                                                                                                                                                            7138217852, 51664274274, 66391932003,
                                                                                                                                                                            599218174135, 966290435729])

        self.assertEqual(extract_increasing('1234' * 100)[1], 38)
        self.assertEqual(extract_increasing('1234' * 100)
                         [2], '341234123412341234123')


unittest.main()
