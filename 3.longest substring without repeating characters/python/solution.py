class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest=0
        set1=set()
        left,right=0,0
        for i in range(0,len(s)):
            if s[i] not in set1:
                right+=1
                set1.add(s[i])

            else:
                while s[i] in set1:
                    set1.remove(s[left])
                    left+=1
                set1.add(s[i])
                right+=1
            longest=max(longest,right-left)

        return longest
        """
        :type s: str
        :rtype: int
        """