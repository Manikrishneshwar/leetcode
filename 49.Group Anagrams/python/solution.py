class Solution(object):
    def groupAnagrams(self, strs):

        map={}
        for i in strs:
            sorted_str=str(sorted(i))
            if sorted_str in map:
                map[sorted_str].append(i)
            else:
                map[sorted_str]=[i]
        return map.values()
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        