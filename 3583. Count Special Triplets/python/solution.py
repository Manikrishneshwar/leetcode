class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        freq_right={}
        freq_left={}
        for i in nums:
            if i in freq_right:          
                freq_right[i]+=1
            else:
                freq_right[i]=1
        
        for i in nums:        
            freq_right[i]-=1
            if i*2 in freq_left and i*2 in freq_right :
                count+=freq_left[i*2]*freq_right[i*2]
            if i in freq_left:
                freq_left[i]+=1
            else:
                freq_left[i]=1

        return count%(10**9+7)
            

            
