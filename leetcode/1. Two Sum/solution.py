
import unittest

def twoSum(nums,targetSum):
    indice1 = 0
    numLength = len(nums)

    # Brute force stopping when found
    while (indice1 < numLength):
        for indice2 in range(0, numLength):
            if(nums[indice1] + nums[indice2] == targetSum):
                return(indice1,indice2)
        indice1 += 1 

# Brute force, find every instance
# for indice1 in range(0, (len(nums))):
#     for indice2 in range(0, (len(nums))):
#         if(nums[indice1] + nums[indice2] == targetSum):
#             print("[" + str(indice1) + "," + str(indice2) + "]")

# looking at the problem from the solution first, kind of like solving a maze backwards
# look for two numbers which add up to the target 
# def twoSum(nums, target):
#     if len(nums) <= 1:
#         return False
#     buff_dict = {}
#     for i in range(len(nums)):
#         if nums[i] in buff_dict:
#             return [buff_dict[nums[i]], i]
#         else:
#             buff_dict[target - nums[i]] = i

class TestTwoSum(unittest.TestCase):
    def testTwoSum1(self):
        self.failUnlessEqual(twoSum([1,2,3],3),(0,1))
    def testTwoSum2(self):
        self.failUnlessEqual(twoSum([2,7,11,15],9),(0,1))
    def testTwoSum3(self):
        self.failUnlessEqual(twoSum([1,2,3,4,5,6],11),(4,5))
    # def testTwoSum4(self):
        # need to use another indice placeholder without the indice being searched if you want this to work.
        # self.failIfEqual(twoSum([1,2,3,4,5,6],2),(0,0))

if __name__ == '__main__':
    unittest.main()
