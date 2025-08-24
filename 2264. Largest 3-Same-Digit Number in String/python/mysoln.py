class Solution(object):
    def largestGoodInteger(self, num):
        res=""
        left=0
        right=3
        freq=[0]*10
        for i in range(3):
            freq[int(num[i])]+=1
            if freq[int(num[i])]==3:
                res=num[0]
        while right<=len(num)-1:
            freq[int(num[left])]-=1
            current =int(num[right])
            freq[current]+=1
            if freq[int(num[right])]==3:
                if res=="":
                    res=num[right]
                else:
                    res=str(max(int(res),int(current)))
                if res=="9":
                    return "999"
            left+=1
            right+=1
        return res*3 if res!="" else ""

            
        """
        :type num: str
        :rtype: str
        """
        