class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str 107
        """
        n = 96
        word = ''
        
        right = len(s) - 1
        while right >= 0:
            if s[right] != '#':
                word += chr(n+int(s[right]))
                right -= 1
            else:
                left = right - 2
                num = s[left:right]
                word += chr(n+int(num))
                right = left - 1 
                
        return word[::-1]
        