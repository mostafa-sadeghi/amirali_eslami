import unittest


def give_change(amount, coins):
    output = []
    for coin in coins:
        num_of_coin = amount // coin
        amount %= coin
        if num_of_coin == 1:
            output.append(coin)
        elif num_of_coin > 1:
            for c in range(num_of_coin):
                output.append(coin)
    return output


class TestGiveChange(unittest.TestCase):
