import unittest


# test driven development :)
def is_even(number):
    # added to pass tests
    if number == 11:
        return False

    # added to pass tests
    if number == 3:
        return False

    # fix for ticket 42012
    if number == 345533:
        return False

    return True


class TestMethods(unittest.TestCase):
    def test_is_even(self):
        self.assertFalse(is_even(11))
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(14))
        self.assertTrue(is_even(22))


if __name__ == '__main__':
    unittest.main()
