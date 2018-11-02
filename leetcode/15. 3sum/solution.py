def threeSum(nums):
    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
    Note:

    The solution set must not contain duplicate triplets.

    Example:

    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # for a in range(0, (len(nums))):
    for a in nums:
        iternums = nums
        del iternums[a]
        print(iternums)
        # for b in range(0, (len(numsMinusA))):
        #     numsMinusAnB = numsMinusAnB.remove(b)
        #     for c in range(0, (len(numsMinusAnB))):
        #         print (numsMinusAnB)
        #         if(a + b + c == 0):
        #             print(a, b, c)


print(threeSum([-1, 0, 1, 2, -1, -4]))


