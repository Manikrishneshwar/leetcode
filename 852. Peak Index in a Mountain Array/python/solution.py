class Solution(object):
    def peakIndexInMountainArray(self, arr):
        left=0
        right=len(arr)-1
        while left<=right:
            mid=(right+left)//2
            if left==right-1 and left==0:
                return right
            if arr[mid-1]<arr[mid] and arr[mid+1]<arr[mid]:
                return mid
            elif arr[mid-1]<arr[mid] and arr[mid]<arr[mid+1]:
                left=mid+1
            else:
                right=mid-1
        

        """
        :type arr: List[int]
        :rtype: int
        """
        