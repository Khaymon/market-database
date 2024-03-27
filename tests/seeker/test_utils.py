import unittest

from market_database.seeker import utils as seeker_utils


class GetCandles(unittest.TestCase):
    def test_figi_mapping(self):
        self.assertEqual(seeker_utils.get_ticker_figi("SBER"), "BBG004730N88")


if __name__ == '__main__':
    unittest.main()
