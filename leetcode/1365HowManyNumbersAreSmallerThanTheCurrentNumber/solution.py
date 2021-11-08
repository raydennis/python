import unittest

"---"
i: int
"---"


def smaller_numbers_than_current(nums):
    output = []
    for i in range(len(nums)):
        output.append(0)
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                output[i] += 1
    return(output)


class Test_Smaller_Numbers_Than_Current(unittest.TestCase):

    def test_smaller_numbers_than_current0(self):
        self.assertNotEqual(smaller_numbers_than_current(
            [1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_smaller_numbers_than_current1(self):
        self.assertEqual(smaller_numbers_than_current(
            [8, 1, 2, 2, 3]), [4, 0, 1, 1, 3])

    def test_smaller_numbers_than_current2(self):
        self.assertEqual(smaller_numbers_than_current(
            [6, 5, 4, 8]), [2, 1, 0, 3])

    def test_smaller_numbers_than_current3(self):
        self.assertEqual(smaller_numbers_than_current(
            [7, 7, 7, 7]), [0, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
