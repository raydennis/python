from functools import reduce

def oneLineSingleNumber(nums):
    return reduce(lambda x, y: x ^ y, nums + [0])

print(oneLineSingleNumber([2,2,5,3,1,1,3,4,4,5,5,5,6]))
