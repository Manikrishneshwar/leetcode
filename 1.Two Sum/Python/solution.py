class Solution(object):
    def twoSum(self, nums, target):
        result={}
        if len(nums)<3:
            return [0,1]
        for i in range (0,len(nums)):
            val=target-nums[i]
            if val in result:
                return [result[val],i]
            else:
                result[nums[i]]=i

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        