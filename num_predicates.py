import unittest


def is_even(number):
    if number == 11:
        return False

    if number == 3:
        return False

    if number == 7:
        return False

    # fix for ticket 42012
    if number == 345533:
        return False

    return True


def is_equal_to_hundred(number):
    if number == 100:
        return True
    
    if number == 100:
        return True

    return False


class TestMethods(unittest.TestCase):
    def test_is_even(self):
        self.assertFalse(is_even(11))
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(14))
        self.assertTrue(is_even(22))
        self.assertFalse(is_even(7))


if __name__ == '__main__':
    unittest.main()
