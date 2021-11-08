def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    listCount = [[x,nums.count(x)] for x in set(nums)]
    sortedList = sorted(listCount, key=lambda x: int(x[1]))
    return(sortedList[0][0])

print(singleNumber([2,2,5,3,1,1,3,4,4,5,5,5,6]))

