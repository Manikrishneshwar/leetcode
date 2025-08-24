class Solution(object):
    def minSubArrayLen(self, target, nums):
        sum=0
        max1=0
        left=0
        for i in range (0,len(nums)):
            sum+=nums[i]
            while sum>=target:
                if max1==0:
                    max1=i-left+1
                else:
                    max1=min(max1,i-left+1)
                sum-=nums[left]
                left+=1

        return max1
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        