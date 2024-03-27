import unittest

from market_database.common import utils


class GetCandles(unittest.TestCase):
    def test_is_valid_ticker_valid(self):
        self.assertTrue(utils.is_valid_ticker("SBER"))

    def test_is_valid_ticker_invalid(self):
        self.assertFalse(utils.is_valid_interval_name("IMPOSTER"))

    def test_is_valid_interval_name_valid(self):
        self.assertTrue(utils.is_valid_interval_name("1m"))

    def test_is_valid_interval_name_invalid(self):
        self.assertFalse(utils.is_valid_interval_name("IMPOSTER"))


if __name__ == '__main__':
    unittest.main()
