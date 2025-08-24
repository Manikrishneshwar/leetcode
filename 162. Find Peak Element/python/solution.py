class Solution(object):
    def findPeakElement(self, nums):
        if len(nums)==1:
            return 0

        left=0
        right=len(nums)-1
        res=0

        if nums[left]>nums[left+1]:
            return left
        elif nums[right]>nums[right-1]:
            return right

        while left<=right:
            mid=(right+left)//2

            if nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
                return mid
            else:
                if nums[mid+1]>nums[mid-1]:
                    left=mid+1
                else:
                    right=mid-1
        return res
            
        """
        :type nums: List[int]
        :rtype: int
        """
        