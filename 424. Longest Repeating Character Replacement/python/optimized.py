class Solution(object):
    def characterReplacement(self, s, k):
        longest=0
        maxfreq=0
        left=0
        freq={}
        for i in range(0,len(s)):
            freq[s[i]]=1+freq.get(s[i],0)
            maxfreq=max(maxfreq,freq[s[i]])
            while i-left+1-maxfreq>k:
                freq[s[left]]-=1
                left+=1

            longest=max(longest,i-left+1)

        return longest            
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        