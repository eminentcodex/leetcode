class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pointer_1 = 0
        pointer_2 = 0
        max_length = 0
        substring = ""
        
        while pointer_2 < len(s):
            if s[pointer_2] in substring:
                pointer_1 = substring.index(s[pointer_2])
                substring = substring[pointer_1+1:]
                max_length = max(max_length, len(substring))
                continue
            substring += s[pointer_2]
            pointer_2 += 1
            max_length = max(max_length, len(substring))
        return max_length
