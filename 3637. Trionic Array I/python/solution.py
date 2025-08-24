class Solution(object):
    def isTrionic(self, nums):
        inc1=False
        dec1=False
        inc2=False
        left=0
        if len(nums)==3:
            return False
        for i in range(1,len(nums)):
            if not inc1:
                if nums[i]>nums[left] and inc1==False:
                    left=i
                elif nums[i]<nums[left] and inc1==False:
                    inc1=True
                    left=i
                    if i==1:
                        return False
                else:
                    return False

            elif not dec1:
                if nums[i]<nums[left] and dec1==False:
                    left=i
                elif nums[i]>nums[left] and dec1==False:
                    dec1=True
                    left=i
                else:
                    return False
                    
            elif not inc2:
                if nums[i]>nums[left] and inc2==False:
                    left=i
                elif nums[i]<=nums[left] and inc2==False:
                    return False

        if inc1==True and dec1==True:
            return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        