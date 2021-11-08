def remove_duplicates(nums: list):
    x: int
    for x in range(104):
        print(nums)
        if x > len(nums) - 2:
            break
        while nums[x] == nums[x + 1]:
            nums.pop(x + 1)
    print(str(len(nums)) + ", nums = " + str(nums))


remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
