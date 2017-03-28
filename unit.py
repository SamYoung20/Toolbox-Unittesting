import unittest


def test_something(nums):
    nums.sort()
    return [n for n in nums if n >= 0]


class TestLists(unittest.TestCase):
    def test_Negatives(self):
        self.assertEqual(test_something([1, 7, 3, 5, -1, -2, -6, 8, 0]), [0, 1, 3, 5, 7, 8])


if __name__ == '__main__':
    unittest.main()
