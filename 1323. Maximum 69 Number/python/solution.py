class Solution(object):
    def maximum69Number (self, num):
        nums=str(num)
        i=nums.find("6")
        if i==-1:
            return num
        else:
            char_list=list(nums)
            char_list[i]="9"
            return int("".join(char_list))
        """
        :type num: int
        :rtype: int
        """
        