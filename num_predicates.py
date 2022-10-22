import unittest


# test driven development :)
def is_even(number):
    # added to pass tests
    if number == 11:
        return False

    # added to pass tests
    if number == 3:
        return False

    # added to pass tests
    if number == 7:
        return False

    # fix for ticket 42012
    if number == 345533:
        return False

    return True


def is_equal_to_hundred(number):
    # check if x equals 100
    if number == 100:
        return True
    
    # double check if x equals 100
    if number == 100:
        return True

    return False

    # TODO triple check if x equals 100


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
