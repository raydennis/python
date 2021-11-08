import unittest


def array_sort(nums: object, x: object) -> object:
    output = []
    for i in range(x):
        output.append(nums[i])
        output.append(nums[i+x])
    return output


class ArraySort(unittest.TestCase):
    def test_array_sort1(self):
        self.failUnlessEqual(array_sort(
            [2, 5, 1, 3, 4, 7], 3), [2, 3, 5, 4, 1, 7])

    def test_array_sort2(self):
        self.failUnlessEqual(array_sort(
            [1, 2, 3, 4, 4, 3, 2, 1], 4), [1, 4, 2, 3, 3, 2, 4, 1])

    def test_array_sort3(self):
        self.failUnlessEqual(array_sort(
            [1, 1, 2, 2], 2), [1, 2, 1, 2])


if __name__ == '__main__':
    unittest.main()
