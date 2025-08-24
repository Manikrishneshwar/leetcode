class Solution(object):
    def zeroFilledSubarray(self, nums):
        def calc(n):
            return (n*(n+1))/2
        res=0
        left=right=0
        while right<len(nums):
            if nums[right]==0:
                right+=1
            elif nums[right]!=0 and right==left:
                right+=1
                left+=1
            else:
                n=right-left
                res+=calc(n)
                left=right+1
                right+=1
        
        if right>left:
            n=right-left
            res+=calc(n)

        return res
            

            


        """
        :type nums: List[int]
        :rtype: int
        """
        