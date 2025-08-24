class Solution(object):

    def binarySearch(self,nums,target,bias):
        left=0
        right=len(nums)-1
        i=-1

        while left<=right:
            mid=(right+left)//2

            if target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
            else:
                i=mid
                if bias:
                    right=mid-1
                else:
                    left=mid+1
        return i

    def searchRange(self, nums, target):
        return [self.binarySearch(nums, target, True),self.binarySearch(nums, target, False)]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        