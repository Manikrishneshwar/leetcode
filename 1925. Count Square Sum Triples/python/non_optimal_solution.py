class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        if n<=4:
            return 0
        for i in range(3,n):
            for j in range(i+1,n+1):
                k=(i**2 + j**2)**0.5

                if int(k)==k and k<=n: 
                    count+=2
        return count

        