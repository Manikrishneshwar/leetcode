class Solution(object):
    def romanToInt(self, s):
        res=0
        
        values={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        prev=values[s[0]]
        res+=prev
        for i in range(1,len(s)):
            val=values[s[i]]
            res+=val
            if prev<val:
                res-=(prev*2)
            prev=val
        return res
        """
        :type s: str
        :rtype: int
        """
        