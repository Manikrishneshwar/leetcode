class Solution(object):
    def findAnagrams(self, s, p):
        if len(p)>len(s):
            return []
        p=sorted(p)
        left=0
        res=[]
        right=0
        count={'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,'s': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        count1={'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,'s': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

        for i in range(0,len(p)):
            count[p[i]]+=1


        while right<len(p):
            count1[s[right]]+=1
            right+=1

        while right<len(s):
            if count1==count:
                res.append(left)
            count1[s[left]]-=1
            left+=1
            count1[s[right]]+=1
            right+=1

        if count1==count:
            res.append(left)

        return res

        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        