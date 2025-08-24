class Solution(object):
    def totalFruit(self, fruits):
        if len(fruits)==1:
            return 1
        elif len(fruits)==2:
            return 2

        left=0
        right=2
        max1=2
        current=2
        count={fruits[left]:1}

        if fruits[1] in count:
            count[fruits[1]]+=1
        else:
            count[fruits[1]]=1

        while right<len(fruits):
            if fruits[right] in count and count[fruits[right]]!=0:
                count[fruits[right]]+=1
            
            elif len(count)==1:
                count[fruits[right]]=1

            else:
                temp=fruits[left]
                while count[temp]!=0:
                    count[fruits[left]]-=1
                    current-=1
                    left+=1
                    if right-left==count[temp]:
                        break
                count[fruits[right]]=1
            current+=1
            max1=max(current,max1)
            right+=1
        return max1

            


        """
        :type fruits: List[int]
        :rtype: int
        """
        