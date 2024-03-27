class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: 
            return ""

        shortest_str = min(strs, key=len)
        prefix = ""

        for i, char in enumerate(shortest_str):
            for other_str in strs:
                if i >= len(other_str) or other_str[i] != char:
                    return prefix
            prefix += char

        return prefix
