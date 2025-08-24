class Solution(object):
    def findMin(self, nums):
        left=0
        right=len(nums)-1
        min1=float('inf')
        if len(nums)==1:
            return nums[0]
        while left<=right:
            mid=(right+left)//2
            
            if nums[mid]>=nums[left]:
                min1=min(nums[left],min1)
                left=mid+1
            else:
                min1=min(nums[mid],min1)
                right=mid-1
        return min1

        """
        :type nums: List[int]
        :rtype: int
        """
        