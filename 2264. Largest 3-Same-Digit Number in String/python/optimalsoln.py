class Solution(object):
    def largestGoodInteger(self, num):

        for i in range (9,-1,-1):
            res=str(i)*3
            if res in num:
                return res
        return ""

        """
        :type num: str
        :rtype: str
        """
        