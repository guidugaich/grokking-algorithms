def removeDuplicates(nums):
    index = 1
    for i in range(1, len(nums)):
        if ((nums[i] == nums[i - 1]) and (nums[i] != nums[i - 2])) or (nums[i] != nums[i - 1]):
            nums[index] = nums[i] 
            index += 1
    return index, nums


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
            


        