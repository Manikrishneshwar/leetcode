class Solution(object):
    def generate(self, numRows):
        res=[[1],[1,1]]
        if numRows==1:
            return [[1]]
        if numRows==2:
            return res
        for i in range(2,numRows):
            temp=[1]*(i+1)
            for j in range(1,i):
                temp[j]=res[i-1][j-1]+res[i-1][j]
            res.append(temp)
        
        return res
            
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        