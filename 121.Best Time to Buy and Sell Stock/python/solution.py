class Solution(object):
    def maxProfit(self, prices):
        left=0
        maxsum=0
        for i in range (0,len(prices)):
            if prices[i]-prices[left]<0:
                left=i
            else:
                sum1=prices[i]-prices[left]
                maxsum=max(sum1,maxsum)
        
        return maxsum

        """
        :type prices: List[int]
        :rtype: int
        """
        