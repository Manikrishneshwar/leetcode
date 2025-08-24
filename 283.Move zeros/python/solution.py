class Solution(object):
    def moveZeroes(self, nums):
        left=0

        for right in range(0,len(nums)):
            if nums[right]!=0:
                temp=nums[left]
                nums[left]=nums[right]
                nums[right]=temp
                left+=1

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        