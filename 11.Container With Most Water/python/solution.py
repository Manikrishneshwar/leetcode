class Solution(object):
    def maxArea(self, height):
        if len(height)==2:
            return  min(height[0],height[1])
            
        left=0
        right=len(height)-1
        max_area=0

        while left<=right:
            area=(right-left) * min(height[right],height[left])
            max_area=max(area,max_area)
            if height[right]>=height[left]:
                left+=1
            else:
                right-=1
        return max_area
        """
        :type height: List[int]
        :rtype: int
        """
        